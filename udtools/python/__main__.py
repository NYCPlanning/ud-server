import sys
import click

__version__ = "1.0.0"

@click.group()
@click.version_option(__version__)
def main():
    """A CVE Search and Lookup CLI"""
    print("Hye")
    pass
    
@main.command()
@click.argument('keyword', required=False)
def search(**kwargs):
    """Search through CVE Database for vulnerabilities"""
    click.echo(kwargs)
    pass
    
@main.command()
@click.argument('name', required=False)
def look_up(**kwargs):
    """Get vulnerability details using its CVE-ID on CVE Database"""
    click.echo(kwargs)
    pass
    
if __name__ == '__main__':
  args = sys.argv
  if "--help" in args or len(args) == 1:
    print(f"UDTools {__version__}")
  main()