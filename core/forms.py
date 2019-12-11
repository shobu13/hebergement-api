from django import forms
from django.core.validators import RegexValidator

placeholders = {
    "description": """Soyez clair et concis et donnez un maximum de détails sur vous et votre situation.""",
    "radius": """ratissez large pour augmenter vos chances.""",
    "compensations": """que pouvez vous apporter à votre futur logeur ?
    - bricolage
    - lessive
    - vaisselle
    - ect...""",
    "addictions": """Soyez franc, rien ne sert de mentir."""
}


class BaseUserForm(forms.Form):
    last_name = forms.CharField(max_length=100, label="Nom", widget=forms.TextInput)
    first_name = forms.CharField(max_length=100, label="Prénom", widget=forms.TextInput)
    mail = forms.EmailField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirmer", widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10, validators=[
        RegexValidator("^0[1-9]([-. ]?[0-9]{2}){4}$", message="Numéro sous forme 0728288002")], required=False,
                                   label="Téléphone (facultatif)", widget=forms.TextInput)
    city_id = forms.CharField(label="Code postal",
                              widget=forms.TextInput(attrs={'class': 'form-control basicAutoComplete'}),
                              min_length=5, max_length=5, validators=[RegexValidator('^[0-9]{5,5}$')])
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": placeholders["description"]}))

    def __init__(self, *args, **kwargs):
        super(BaseUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not self.fields[field].widget.attrs.get('class', None):
                self.fields[field].widget.attrs['class'] = 'form-control'


class HostedForm(BaseUserForm):
    radius = forms.IntegerField(label="Rayon de recherche (km)",
                                widget=forms.NumberInput(attrs={"placeholder": placeholders["radius"]}))
    compensations = forms.CharField(widget=forms.Textarea(attrs={"placeholder": placeholders["compensations"]}))
    addictions = forms.CharField(widget=forms.Textarea(attrs={"placeholder": placeholders["addictions"]}))
    file = forms.FileField(label="vidéo de présentation (facultatif)", widget=forms.FileInput(attrs={
        'class': 'filestyle',
        'data-text': "choisir un fichier",
        'data-placeholder': "choisir une vidéo pour vous présenter (facultatif)"
    }), required=False)
