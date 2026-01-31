from django import forms
from .models import Project
class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Project
        fields = ['project_name','brief','status','start_date','end_date','aircraft','no_meetings','iom_tm','no_sorties','trials']
        widgets = {'brief': forms.Textarea(attrs={'rows':4}),'aircraft': forms.TextInput(attrs={'placeholder':'e.g. LSP6, PV3, Bomb X'})}
    
    fields = [
    'project_name','brief','status',
    'start_date','end_date','aircraft',
    'no_meetings','iom_tm','no_sorties','trials',
    'miscellaneous_reason','marked_reason','marked_by','attachment'
]