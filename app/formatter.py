class Formatter:

    @staticmethod
    def format_size(size_bytes: int) -> str:
        mb = size_bytes / (1024 * 1024)
        return f"{mb:.2f} MB"

    @staticmethod
    def print_images(numbered_images):
        print("\n🧹 DockerStrange — Master of the Multilayers\n")
        print("---------------------------------------------------")

        for index, image in numbered_images:
            tags = image.tags or ["<none>:<none>"]
            size = image.attrs.get("Size", 0)
            size_str = Formatter.format_size(size)

            print(f"{index}. {tags[0]} | {size_str}")

        print("---------------------------------------------------")
