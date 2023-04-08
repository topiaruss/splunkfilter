import click
import regexs
import re


@click.option("--ip", default="", help="optional ip address")
@click.option("--method", default="", help="optional method")
@click.option("--uri", default="", help="uri substring")
@click.option("--protocol", default="", help="for example HTTP")
@click.option("--protocol_version", default="", help="for example 1.1")
@click.option("--operation", default="or", help="operation - default or",
              type=click.Choice(['OR', 'AND'], case_sensitive=False))
@click.command()
def main(ip, method, uri, protocol, protocol_version, operation):
    operator = any if operation in ["or","OR"] else all

    with click.get_text_stream("stdin") as input_stream, click.get_text_stream(
        "stdout"
    ) as output_stream:
        for line in input_stream:
            match = re.match(regexs.www_single, line)
            if match:
                if operator(
                    (
                        ip and match["client_ip"] == ip,
                        method and match["request_method"] == method,
                        uri and uri in match["request_uri"],
                        protocol and match["protocol"] == protocol,
                        protocol_version and match["protocol_version"] == protocol_version,
                    )
                ):
                    output_stream.write(line)


if __name__ == "__main__":
    main()
