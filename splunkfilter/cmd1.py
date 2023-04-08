import click
import regexs
import re


@click.command()
def main():
    with click.get_text_stream("stdin") as input_stream, click.get_text_stream(
        "stdout"
    ) as output_stream:
        for line in input_stream:
            output_stream.write(line)


if __name__ == "__main__":
    main()
