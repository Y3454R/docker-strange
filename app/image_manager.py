class ImageManager:
    def __init__(self, docker_client):
        self.docker_client = docker_client
        self.images = []

    def load_images(self):
        self.images = self.docker_client.list_images()

    def get_numbered_images(self):
        return list(enumerate(self.images, start=1))

    def delete_by_index(self, index: int, force: bool = True):
        if index < 1 or index > len(self.images):
            raise ValueError("Invalid image number.")

        image = self.images[index - 1]
        self.docker_client.remove_image(image.id, force=force)
