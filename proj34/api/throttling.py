from rest_framework.throttling import UserRateThrottle


class RegRateThrottle(UserRateThrottle):
    scope = 'reg'