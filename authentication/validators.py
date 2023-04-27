from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une Lettre', code='password_no_letters')
    
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'


class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(character.isdigit() for character in password):
            raise ValidationError(
                'Le mot de passe doit contenir des chiffres', code='password_no_digits'
            )
    
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un chiffre.'