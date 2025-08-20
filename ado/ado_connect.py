import argparse,sys,json,time,os
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication


class ReleaseExecutionContext:
    status_order = {
        "queued": 1,
        "notStarted": 2,
        "succeeded": 3,
        "inProgress": 4

    }
    printed_statuses = []
    activeTasks = []
    failedTasks = []

    def __init__(self, release_client, project_id, release):
        self.release_client = release_client
        self.project_id = project_id
        self.release = release
        self.activeTasks = [stage for stage in self.release.environments if stage.status in ['inProgress','notStarted','queued']]


    def refresh(self):
        self.release = self.release_client.get_release(self.project_id, self.release.id)
        self.activeTasks = [stage for stage in self.release.environments if stage.status in ['inProgress','notStarted','queued']]
        self.failedTasks = [stage for stage in self.release.environments if stage.status in ['failed','rejected']]


    def isRunning(self):
        return len(self.activeTasks)>0 and len(self.failedTasks)==0


    def isSucessfull(self):
        return len(self.release.environments) == len([stage for stage in self.release.environments if stage.status == 'succeeded'])


    def print_status(self):

        stages = sorted(self.release.environments, key=lambda stage : self.status_order[stage.status] if stage.status in self.status_order  else  1000)

        for stage in stages:
            stage_status = f"{stage.name}: {stage.status}"
            if stage_status not in self.printed_statuses:
                if stage.status == 'succeeded':
                    print("")
                print(stage_status)
            else:
                print(".", end="")
            self.printed_statuses.append(stage_status)

class ADOReleaseRunner:

    def __init__(self, client, project_id):
        self.client = client
        self.project_id = project_id

    def run_release(self, release_meta_data):
        release = self.client.create_release(release_meta_data, self.project_id)
        print(f"Triggered Release Pipeline [{release.release_definition.name}] - Release Id: {release.name}")
        return ReleaseExecutionContext (self.client, self.project_id, release)


def main(args):
    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', '-T', action='store', default=None, required=False)
    parser.add_argument('--ado_url', '-U', action='store', default="https://dev.azure.com", required=False)
    parser.add_argument('--collection', '-C', action='store', required=True)
    parser.add_argument('--project', '-P', action='store', required=True)
    # parser.add_argument('--json_payload', '-d', action='store', required=False)
    # parser.add_argument('--wait', '-w', action='store_true', default=False, required=False)
    # parser.add_argument('--poll_interval', '-i', action='store', default=10, required=False)

    args = parser.parse_args(args)

    personal_access_token = args.token
    organization_url = f"{args.ado_url}/{args.collection}"
    credentials = BasicAuthentication('', personal_access_token)

    ado_connection = Connection(base_url=organization_url, creds=credentials)

    release_client = ado_connection.clients.get_release_client()





    # ado_runner = ADOReleaseRunner(release_client, args.project)
    # release_ctx = ado_runner.run_release(release_meta_data = release_metadata)
    # print(f"Release URL: {release_ctx.release.url}")
    #
    # if args.wait:
    #     while release_ctx.isRunning():
    #         release_ctx.refresh()
    #         release_ctx.print_status()
    #         time.sleep(args.poll_interval)
    #
    #     if release_ctx.isSucessfull():
    #         print(f"Pipeline [{release_ctx.release.release_definition.name}] Successfully Completed")
    #     else:
    #         print(f"Pipeline [{release_ctx.release.release_definition.name}] Failed.")
    #         print(f"Pipeline failed on:")
    #         for t in release_ctx.failedTasks:
    #             print(f"{t.name}: {t.status}")
    #         sys.exit(1)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))