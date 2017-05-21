from django import forms


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
# class SubscriberForm(forms.ModelForm):
#
#     class Meta:
#         model = Subscriber
#         exclude = [""]
#
