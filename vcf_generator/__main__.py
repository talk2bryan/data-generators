"""CLI module for vcf_generator package.

The user can either call the gen_contacts module or the gen_vcards module as follows:

$ python -m vcf_generator contacts_str [--num_contacts NUM_CONTACTS] [--output_file OUTPUT_FILE]
$ python -m vcf_generator vcards [--num_contacts NUM_CONTACTS] [--output_file OUTPUT_FILE]
"""

import fire

from vcf_generator import MIN_NUM_CONTACTS
from vcf_generator.gen_contacts import main as gen_contacts
from vcf_generator.gen_vcards import main as gen_vcards


class Contacts:
    """CLI module for vcf_generator package."""

    def contacts_str(
        self,
        num_contacts: int = MIN_NUM_CONTACTS,
        output_file: str | None = None,
    ):
        """Generate contacts as.
        Use -n to specify the number of contacts to generate and -o to specify an output file.

        Args:
            num_contacts (int, optional): Number of contacts to generate. Defaults to MIN_NUM_CONTACTS.
            output_file (str | None, optional): Output file path. Defaults to None.
        """
        gen_contacts(num_contacts=num_contacts, output_file=output_file)

    def vcards(
        self,
        num_contacts: int = MIN_NUM_CONTACTS,
        output_file: str | None = None,
    ):
        """Generate vCards.
        Use -n to specify the number of contacts to generate and -o to specify an output file.

        Args:
            num_contacts (int, optional): Number of contacts to generate. Defaults to MIN_NUM_CONTACTS.
            output_file (str | None, optional): Output file path. Defaults to None.
        """
        gen_vcards(num_contacts=num_contacts, output_file=output_file)


def main():
    fire.Fire(Contacts)


if __name__ == "__main__":
    main()
