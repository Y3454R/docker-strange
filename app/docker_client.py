import docker
from docker.errors import APIError


class DockerClient:
    def __init__(self):
        self.client = docker.from_env()

    def list_images(self):
        return self.client.images.list()

    def remove_image(self, image_id: str, force: bool = False):
        try:
            self.client.images.remove(image_id, force=force)
        except APIError as e:
            raise RuntimeError(f"Failed to remove image: {e}")
