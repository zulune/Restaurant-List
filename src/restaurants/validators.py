from django.core.exceptions import ValidationError


def validate_email(value):
    email = value
    if ".edu" in email:
        raise forms.ValidationError("We do not accept .edu emails")


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']


def validate_category(value):
    print(value)
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError("{} is not a valid category".format(value))
