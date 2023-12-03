class HealthDomainService:
    def __init__(self):
        self.user_count = 0

    def get_health_status(self):

        return {
            "status": "OK",
            "user_count": self.user_count,
        }
