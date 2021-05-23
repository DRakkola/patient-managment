from django.db import models
from django.contrib.auth.models import User

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class AccountsUsergroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'accounts_usergroups'


class AccountsUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_full_name_displayed = models.BooleanField()
    bio = models.CharField(max_length=500, blank=True, null=True)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)
    group = models.ForeignKey(AccountsUsergroups, models.DO_NOTHING, db_column='Group_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_userprofile'


class AccountsUserprofileRights(models.Model):
    id = models.BigAutoField(primary_key=True)
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    userrights = models.ForeignKey('AccountsUserrights', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_userprofile_Rights'
        unique_together = (('userprofile', 'userrights'),)


class AccountsUserrights(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    details = models.CharField(db_column='Details', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_userrights'


class Allergiques(models.Model):
    allerg_1 = models.CharField(max_length=255, blank=True, null=True)
    allerg_2 = models.CharField(max_length=255, blank=True, null=True)
    allerg_3 = models.CharField(max_length=255, blank=True, null=True)
    allerg_4 = models.BooleanField(blank=True, null=True)
    allerg_5 = models.CharField(max_length=255, blank=True, null=True)
    allerg_6 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allergiques'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CardioVasculaire(models.Model):
    card_1 = models.BooleanField(blank=True, null=True)
    card_2 = models.BooleanField(blank=True, null=True)
    card_3 = models.BooleanField(blank=True, null=True)
    card_4 = models.BooleanField(blank=True, null=True)
    card_5 = models.BooleanField(blank=True, null=True)
    card_6 = models.BooleanField(blank=True, null=True)
    card_7 = models.BooleanField(blank=True, null=True)
    card_8 = models.BooleanField(blank=True, null=True)
    card_9 = models.BooleanField(blank=True, null=True)
    card_10 = models.CharField(max_length=255, blank=True, null=True)
    card_11 = models.DateField(blank=True, null=True)
    card_12 = models.BooleanField(blank=True, null=True)
    card_13 = models.BooleanField(blank=True, null=True)
    card_14 = models.BooleanField(blank=True, null=True)
    card_15 = models.BooleanField(blank=True, null=True)
    card_16 = models.BooleanField(blank=True, null=True)
    card_17 = models.BooleanField(blank=True, null=True)
    card_18 = models.BooleanField(blank=True, null=True)
    card_19 = models.BooleanField(blank=True, null=True)
    card_20 = models.BooleanField(blank=True, null=True)
    card_21 = models.BooleanField(blank=True, null=True)
    card_22 = models.BooleanField(blank=True, null=True)
    card_23 = models.BooleanField(blank=True, null=True)
    card_24 = models.BooleanField(blank=True, null=True)
    card_25 = models.BooleanField(blank=True, null=True)
    card_26 = models.BooleanField(blank=True, null=True)
    card_27 = models.BooleanField(blank=True, null=True)
    card_28 = models.BooleanField(blank=True, null=True)
    card_29 = models.BooleanField(blank=True, null=True)
    card_30 = models.BooleanField(blank=True, null=True)
    card_31 = models.BooleanField(blank=True, null=True)
    card_32 = models.BooleanField(blank=True, null=True)
    card_33 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cardio_vasculaire'


class Chirurgicaux(models.Model):
    churg_0 = models.BooleanField(blank=True, null=True)
    churg_1 = models.CharField(max_length=255, blank=True, null=True)
    churg_2 = models.CharField(max_length=255, blank=True, null=True)
    churg_3 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chirurgicaux'


class Dentaire(models.Model):
    dent_1 = models.BooleanField(blank=True, null=True)
    img_dentid = models.ForeignKey('ImgDent', models.DO_NOTHING, db_column='img_dentid')
    dent_2 = models.BooleanField(blank=True, null=True)
    dent_3 = models.BooleanField(blank=True, null=True)
    dent_4 = models.BooleanField(blank=True, null=True)
    dent_5 = models.BooleanField(blank=True, null=True)
    dent_6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dentaire'


class Digestifs(models.Model):
    digest_1 = models.BooleanField(blank=True, null=True)
    digest_2 = models.BooleanField(blank=True, null=True)
    digest_3 = models.BooleanField(blank=True, null=True)
    digest_4 = models.BooleanField(blank=True, null=True)
    digest_5 = models.BooleanField(blank=True, null=True)
    digest_6 = models.BooleanField(blank=True, null=True)
    digest_7 = models.BooleanField(blank=True, null=True)
    digest_8 = models.CharField(max_length=255, blank=True, null=True)
    digest_9 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digestifs'


class Divers(models.Model):
    dive_1 = models.BooleanField(blank=True, null=True)
    dive_2 = models.BooleanField(blank=True, null=True)
    dive_3 = models.BooleanField(blank=True, null=True)
    dive_4 = models.CharField(max_length=255, blank=True, null=True)
    dive_5 = models.CharField(max_length=255, blank=True, null=True)
    dive_6 = models.CharField(max_length=255, blank=True, null=True)
    div_7 = models.BooleanField(blank=True, null=True)
    div_8 = models.BooleanField(blank=True, null=True)
    div_9 = models.BooleanField(blank=True, null=True)
    div_10 = models.BooleanField(blank=True, null=True)
    div_11 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'divers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dossier(models.Model):
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientid')
    formid = models.ForeignKey('Form', models.DO_NOTHING, db_column='formid')

    class Meta:
        managed = False
        db_table = 'dossier'


class Enceinte(models.Model):
    a = models.BooleanField(blank=True, null=True)
    b = models.IntegerField(blank=True, null=True)
    c = models.BooleanField(blank=True, null=True)
    g = models.BooleanField(blank=True, null=True)
    h = models.CharField(max_length=255, blank=True, null=True)
    i = models.DateField(blank=True, null=True)
    j = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enceinte'


class Encours(models.Model):
    meds = models.CharField(max_length=255, blank=True, null=True)
    dose = models.CharField(max_length=255, blank=True, null=True)
    matin = models.IntegerField(blank=True, null=True)
    midi = models.IntegerField(blank=True, null=True)
    soir = models.IntegerField(blank=True, null=True)
    nuit = models.IntegerField(blank=True, null=True)
    traitementid = models.ForeignKey('Traitement', models.DO_NOTHING, db_column='traitementid')

    class Meta:
        managed = False
        db_table = 'encours'


class Familiaux(models.Model):
    famil_1 = models.CharField(max_length=255, blank=True, null=True)
    famil_2 = models.CharField(max_length=255, blank=True, null=True)
    famil_3 = models.CharField(max_length=255, blank=True, null=True)
    famil_4 = models.CharField(max_length=255, blank=True, null=True)
    famil_5 = models.BooleanField(blank=True, null=True)
    famil_6 = models.BooleanField(blank=True, null=True)
    famil_7 = models.BooleanField(blank=True, null=True)
    famil_8 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familiaux'


class Form(models.Model):
    cardio_vasculaireid = models.ForeignKey(CardioVasculaire, models.DO_NOTHING, db_column='cardio_vasculaireid')
    pulmonairesid = models.ForeignKey('Pulmonaires', models.DO_NOTHING, db_column='pulmonairesid')
    chirurgicauxid = models.ForeignKey(Chirurgicaux, models.DO_NOTHING, db_column='chirurgicauxid')
    renauxid = models.ForeignKey('Renaux', models.DO_NOTHING, db_column='renauxid')
    neurologiquesid = models.ForeignKey('Neurologiques', models.DO_NOTHING, db_column='neurologiquesid')
    hormonauxid = models.ForeignKey('Hormonaux', models.DO_NOTHING, db_column='hormonauxid')
    digestifsid = models.ForeignKey(Digestifs, models.DO_NOTHING, db_column='digestifsid')
    allergiquesid = models.ForeignKey(Allergiques, models.DO_NOTHING, db_column='allergiquesid')
    hematologiquesid = models.ForeignKey('Hematologiques', models.DO_NOTHING, db_column='hematologiquesid')
    rhumatologiquesid = models.ForeignKey('Rhumatologiques', models.DO_NOTHING, db_column='rhumatologiquesid')
    habitudesid = models.ForeignKey('Habitudes', models.DO_NOTHING, db_column='habitudesid')
    familiauxid = models.ForeignKey(Familiaux, models.DO_NOTHING, db_column='familiauxid')
    dentaireid = models.ForeignKey(Dentaire, models.DO_NOTHING, db_column='dentaireid')
    diversid = models.ForeignKey(Divers, models.DO_NOTHING, db_column='diversid')
    gynecoid = models.ForeignKey('Gyneco', models.DO_NOTHING, db_column='gynecoid')
    pediatriquesid = models.ForeignKey('Pediatriques', models.DO_NOTHING, db_column='pediatriquesid')
    traitementid = models.ForeignKey('Traitement', models.DO_NOTHING, db_column='traitementid')

    class Meta:
        managed = False
        db_table = 'form'


class Fumer(models.Model):
    cigarette = models.IntegerField(blank=True, null=True)
    chicha = models.IntegerField(blank=True, null=True)
    tabagisme = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fumer'


class Gyneco(models.Model):
    gyne_1 = models.BooleanField(blank=True, null=True)
    gyne_2 = models.DateField(blank=True, null=True)
    gyne_3 = models.CharField(max_length=255, blank=True, null=True)
    gyne_4 = models.BooleanField(blank=True, null=True)
    gyne_5 = models.BooleanField(blank=True, null=True)
    gyne_6 = models.IntegerField(blank=True, null=True)
    gyne_7 = models.IntegerField(blank=True, null=True)
    gyne_8 = models.IntegerField(blank=True, null=True)
    gyne_9 = models.BooleanField(blank=True, null=True)
    gyne_10 = models.BooleanField(blank=True, null=True)
    gyne_11 = models.CharField(max_length=255, blank=True, null=True)
    gyne_12 = models.BooleanField(blank=True, null=True)
    gyne_13 = models.BooleanField(blank=True, null=True)
    gyne_14 = models.BooleanField(blank=True, null=True)
    gyne_15 = models.BooleanField(blank=True, null=True)
    gyne_16 = models.BooleanField(blank=True, null=True)
    gyne_17 = models.BooleanField(blank=True, null=True)
    gyne_18 = models.BooleanField(blank=True, null=True)
    enceinteid = models.ForeignKey(Enceinte, models.DO_NOTHING, db_column='enceinteid')

    class Meta:
        managed = False
        db_table = 'gyneco'


class Habitudes(models.Model):
    fumerid = models.ForeignKey(Fumer, models.DO_NOTHING, db_column='fumerid')
    habit_1 = models.BooleanField(blank=True, null=True)
    habit_2 = models.BooleanField(blank=True, null=True)
    habit_3 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habitudes'


class Hematologiques(models.Model):
    hemato_1 = models.BooleanField(blank=True, null=True)
    hemato_2 = models.CharField(max_length=255, blank=True, null=True)
    hemato_3 = models.BooleanField(blank=True, null=True)
    hemato_4 = models.BooleanField(blank=True, null=True)
    hemato_5 = models.CharField(max_length=255, blank=True, null=True)
    hemato_6 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hematologiques'


class Hormonaux(models.Model):
    horm_1 = models.BooleanField(blank=True, null=True)
    horm_2 = models.BooleanField(blank=True, null=True)
    horm_3 = models.BooleanField(blank=True, null=True)
    horm_4 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hormonaux'


class ImgDent(models.Model):
    path = models.CharField(max_length=255, blank=True, null=True)
    discription = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'img_dent'


class Neurologiques(models.Model):
    neuro_1 = models.BooleanField(blank=True, null=True)
    neuro_2 = models.BooleanField(blank=True, null=True)
    neuro_3 = models.BooleanField(blank=True, null=True)
    neuro_4 = models.BooleanField(blank=True, null=True)
    neuro_5 = models.BooleanField(blank=True, null=True)
    neuro_6 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neurologiques'


class Operation(models.Model):
    nature = models.CharField(max_length=255, blank=True, null=True)
    dte = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    chirurgicauxid = models.ForeignKey(Chirurgicaux, models.DO_NOTHING, db_column='chirurgicauxid')

    class Meta:
        managed = False
        db_table = 'operation'


class Patient(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    mlle = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    corps = models.CharField(max_length=255, blank=True, null=True)
    family_stats = models.CharField(max_length=255, blank=True, null=True)
    hospital_service = models.CharField(max_length=255, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Pediatriques(models.Model):
    pediatri_1 = models.BooleanField(blank=True, null=True)
    pediatri_2 = models.BooleanField(blank=True, null=True)
    pediatri_3 = models.BooleanField(blank=True, null=True)
    pediatri_4 = models.BooleanField(blank=True, null=True)
    pediatri_5 = models.BooleanField(blank=True, null=True)
    pediatri_6 = models.CharField(max_length=255, blank=True, null=True)
    pediatri_7 = models.BooleanField(blank=True, null=True)
    pediatri_8 = models.IntegerField(blank=True, null=True)
    pediatri_9 = models.IntegerField(blank=True, null=True)
    pediatri_10 = models.IntegerField(blank=True, null=True)
    pediatri_11 = models.IntegerField(blank=True, null=True)
    pediatri_12 = models.BooleanField(blank=True, null=True)
    pediatri_13 = models.BooleanField(blank=True, null=True)
    pediatri_14 = models.BooleanField(blank=True, null=True)
    pediatri_15 = models.BooleanField(blank=True, null=True)
    pediatri_16 = models.BooleanField(blank=True, null=True)
    pediatri_17 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pediatriques'


class Phone(models.Model):
    number = models.IntegerField(blank=True, null=True)
    discription = models.IntegerField(blank=True, null=True)
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone'


class Pulmonaires(models.Model):
    pulm_1 = models.BooleanField(blank=True, null=True)
    pulm_2 = models.BooleanField(blank=True, null=True)
    pulm_3 = models.BooleanField(blank=True, null=True)
    pulm_4 = models.BooleanField(blank=True, null=True)
    pulm_5 = models.BooleanField(blank=True, null=True)
    pulm_6 = models.BooleanField(blank=True, null=True)
    pulm_7 = models.BooleanField(blank=True, null=True)
    pulm_8 = models.BooleanField(blank=True, null=True)
    pulm_9 = models.BooleanField(blank=True, null=True)
    pulm_10 = models.BooleanField(blank=True, null=True)
    pulm_11 = models.BooleanField(blank=True, null=True)
    pulm_12 = models.BooleanField(blank=True, null=True)
    pulm_13 = models.BooleanField(blank=True, null=True)
    pulm_14 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pulmonaires'


class Renaux(models.Model):
    renau_1 = models.BooleanField(blank=True, null=True)
    renau_2 = models.BooleanField(blank=True, null=True)
    renau_3 = models.BooleanField(blank=True, null=True)
    renau_4 = models.BooleanField(blank=True, null=True)
    renau_5 = models.BooleanField(blank=True, null=True)
    renau_6 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'renaux'


class Rhumatologiques(models.Model):
    rhumatol_1 = models.BooleanField(blank=True, null=True)
    rhumatol_2 = models.BooleanField(blank=True, null=True)
    rhumatol_3 = models.BooleanField(blank=True, null=True)
    rhumatol_4 = models.CharField(max_length=255, blank=True, null=True)
    rhumatol_5 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rhumatologiques'


class Traitement(models.Model):

    class Meta:
        managed = False
        db_table = 'traitement'

# Create your models here.
class UserRights(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    Details = models.CharField(max_length=200 , default='rights details')
    def __str__(self):
        return self.name

class UserGroups(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    #Owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    #Settings
    is_full_name_displayed = models.BooleanField(default=True)

    #details
    bio = models.CharField(max_length=500, blank=True, null=True)
    Group = models.ForeignKey(UserGroups, on_delete=models.SET_NULL, blank=True, null=True)
    Rights = models.ManyToManyField(UserRights,blank=True)
    def __str__(self):
        return self.user.username