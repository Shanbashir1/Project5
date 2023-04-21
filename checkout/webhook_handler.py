from django.http import HttpResponse

class stripeWH_Handler:
    """Handle Stripe WebHooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200)
