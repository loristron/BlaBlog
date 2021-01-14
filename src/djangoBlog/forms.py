from django import forms

class ContacForm(forms.Form):
	full_name 	= forms.CharField(
						label="Nome Completo", 
						max_length=120, 
						widget=forms.TextInput(attrs={
							'class': 'form-control',
							'placeholder': 'Seu Nome',
							}
						)
					)
	email		= forms.EmailField(
						label='Seu Email',
						max_length=120,
						widget=forms.EmailInput(attrs={
								'class': 'form-control',
								'placeholder': 'email@email.com'
							}
						)
					)
	content		= forms.CharField(
					label='Mensagem',
					widget=forms.Textarea(attrs={
							'class': 'form-control',
							'placeholder': 'Digite aqui sua mensagem!',
						}
					)
				)

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		print(email)
		if email.endswith('.edu'):
			raise forms.ValidationError('Não use emails institucionais.')
		return email