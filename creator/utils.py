from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from django.core.mail import send_mail


# Custom user model
AppUser = get_user_model()


class Util:

    @staticmethod
    def send_email_verification(data, request):
        """
        Send an email containing a link to verify the new user.

        data: should be the saved serializer instance.
        request: should be the request instance
        """
        user = AppUser.objects.get(email=data['email'])
        
        token = RefreshToken.for_user(user).access_token
        cur_site = get_current_site(request).domain
        rel_link = reverse("creators_verify_email")
        abs_url = F"http://{cur_site}{rel_link}?token={token}"

        body =  F"Hi \U0001F44B {user.username}.\nThanks for registering to use Openuserdata REST API.\n\n"\
                F"Please click on the link below to verify your email address.\n"\
                F"{abs_url}\n\n"\
                F"This link expires in 3 minutes.\n\n"\
                F"If you did not make this request, please disregard this email.\n\n"\
                F"Love \U0001F499, Mayowa\nCreator: Openuserdata API\n(alias: realestKMA)"

        send_mail(
            subject="Verify Email Address",
            message=body,
            recipient_list=[user.email,],
            from_email="kelvinmayoayeni@gmail.com"
        )


    @staticmethod
    def resend_email_verification(data, request):
        """
        Resend an email containing a link to verify the new user.

        data: should be the saved serializer instance.
        request: should be the request instance
        """
        user = AppUser.objects.get(email=data['email'])

        token = RefreshToken.for_user(user).access_token
        cur_site = get_current_site(request).domain
        rel_link = reverse("creators_verify_email")
        abs_url = F"http://{cur_site}{rel_link}?token={token}"

        body =  F"Hi \U0001F44B {user.username}.\n\n"\
                F"To verify your email address please click on the link below.\n"\
                F"{abs_url}\n\n"\
                F"This link expires in 3 minutes.\n\n"\
                F"If you did not make this request, please disregard this email.\n\n"\
                F"Love \U0001F499, Mayowa\nCreator: Openuserdata API\n(alias: realestKMA)"

        send_mail(
            subject="Verify Email Address",
            message=body,
            recipient_list=[user.email,],
            from_email="Openuserdata"
        )