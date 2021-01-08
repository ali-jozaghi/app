import docker as docker_sdk

docker = docker_sdk.from_env()


class DockerContainer:
    def __init__(self, image_name, container_port, host_port, environment_variables=None, commands=None):
        self._image_name = image_name
        self._container_port = container_port
        self._host_port = host_port
        self._commands = commands
        self._environment_variables = environment_variables
        self._container = None

    def create(self):
        self._container = docker.containers.run(
            image=self._image_name,
            command=self._commands,
            environment=self._environment_variables,
            ports={self._container_port: self._host_port},
            detach=True
        )
        return self._container

    def tear_down(self):
        self._container.kill()
        self._container.remove()

    def is_ready(self):
        self._container.reload()
        return self._container.status == 'running'

    def __enter__(self):
        return self.create()

    def __exit__(self, *args):
        self.tear_down()
