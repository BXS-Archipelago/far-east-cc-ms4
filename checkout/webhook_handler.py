from django.http import HttpResponse

class StripeWH_Handler: 
    """
    Recognise Stripe Webhooks
    """
    def __init__(self,request):
        self.request = request

    def handle_event(self, event):
        """ 
        recognise any generic or unknown webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event[type]}',
            status=200
        )