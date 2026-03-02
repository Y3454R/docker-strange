from app.docker_client import DockerClient
from app.image_manager import ImageManager
from app.formatter import Formatter


def run():
    docker_client = DockerClient()
    manager = ImageManager(docker_client)

    manager.load_images()
    numbered_images = manager.get_numbered_images()

    if not numbered_images:
        print("No Docker images found.")
        return

    Formatter.print_images(numbered_images)

    choice = input("\nEnter image number to vanish (or press Enter to exit): ")

    if not choice.strip():
        print("Exiting the multiverse...")
        return

    try:
        index = int(choice)
        manager.delete_by_index(index)
        print("✨ Image has been erased from this timeline.")
    except Exception as e:
        print(f"⚠ {e}")
