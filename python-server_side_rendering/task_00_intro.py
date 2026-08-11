#!/usr/bin/python3
"""Generate personalized invitation files from a text template."""


def generate_invitations(template, attendees):
    """Generate one invitation file for every attendee."""
    if not isinstance(template, str):
        print(
            "Invalid input type for template: expected str, got "
            f"{type(template).__name__}."
        )
        return

    if not isinstance(attendees, list):
        print(
            "Invalid input type for attendees: expected list, got "
            f"{type(attendees).__name__}."
        )
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print(
            "Invalid input type for attendees: "
            "expected a list of dictionaries."
        )
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = (
        "name",
        "event_title",
        "event_date",
        "event_location",
    )

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + placeholder + "}",
                str(value)
            )

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as output_file:
                output_file.write(invitation)
        except OSError as error:
            print(f"Error writing {filename}: {error}")
