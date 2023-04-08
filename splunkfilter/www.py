import click
import regexs
import re


@click.command()
def main():
    with click.get_text_stream("stdin") as input_stream, click.get_text_stream(
        "stdout"
    ) as output_stream:
        for line in input_stream:
            for match in re.finditer(regexs.www, line):
                if match["client_ip"] == "209.160.24.63":
                    output_stream.write(line)


if __name__ == "__main__":
    main()
