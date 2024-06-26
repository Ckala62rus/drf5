from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self,
            email=None,
            password=None,
            username=None,
            **extra_fields
    ):
        if email:
            email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)
        user.email = email
        user.set_password(password)
        user.save(using=self._db)

    def create_user(
            self,
            email=None,
            password=None,
            username=None,
            **extra_fields
    ):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, username, **extra_fields)

    def create_superuser(
            self,
            email=None,
            password=None,
            username=None,
            **extra_fields
    ):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, username, **extra_fields)
