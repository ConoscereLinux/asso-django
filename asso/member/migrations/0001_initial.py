# Generated by Django 4.2.5 on 2023-10-06 13:59

import asso.member.models
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberQualification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="A short description for this content (not visible in views)",
                        verbose_name="Description",
                    ),
                ),
                (
                    "order",
                    models.SmallIntegerField(
                        default=0,
                        help_text="Object ordering value",
                        verbose_name="Order",
                    ),
                ),
            ],
            options={
                "ordering": ["slug"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "is_removed",
                    models.BooleanField(
                        default=False,
                        editable=False,
                        help_text="Set to True to set as removed or 'soft deleted",
                        verbose_name="Is removed?",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=60, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=60, verbose_name="Last Name"),
                ),
                (
                    "cf",
                    models.CharField(
                        max_length=16,
                        validators=[asso.member.models.check_member_cf],
                        verbose_name="Codice Fiscale",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                        verbose_name="Gender",
                    ),
                ),
                ("birth_date", models.DateField(verbose_name="Birth Date")),
                (
                    "birth_city",
                    models.CharField(
                        help_text="City/municipality or foreign country where Member is born",
                        max_length=150,
                        verbose_name="Birth City",
                    ),
                ),
                (
                    "birth_province",
                    models.CharField(
                        choices=[
                            ("AG", "AGRIGENTO"),
                            ("AL", "ALESSANDRIA"),
                            ("AN", "ANCONA"),
                            ("AO", "AOSTA"),
                            ("AR", "AREZZO"),
                            ("AP", "ASCOLI PICENO"),
                            ("AT", "ASTI"),
                            ("AV", "AVELLINO"),
                            ("BA", "BARI"),
                            ("BL", "BELLUNO"),
                            ("BN", "BENEVENTO"),
                            ("BG", "BERGAMO"),
                            ("BI", "BIELLA"),
                            ("BO", "BOLOGNA"),
                            ("BZ", "BOLZANO"),
                            ("BS", "BRESCIA"),
                            ("BR", "BRINDISI"),
                            ("CA", "CAGLIARI"),
                            ("CL", "CALTANISSETTA"),
                            ("CB", "CAMPOBASSO"),
                            ("CE", "CASERTA"),
                            ("CT", "CATANIA"),
                            ("CZ", "CATANZARO"),
                            ("CH", "CHIETI"),
                            ("CO", "COMO"),
                            ("CS", "COSENZA"),
                            ("CR", "CREMONA"),
                            ("KR", "CROTONE"),
                            ("CN", "CUNEO"),
                            ("EN", "ENNA"),
                            ("FM", "FERMO"),
                            ("FE", "FERRARA"),
                            ("FI", "FIRENZE"),
                            ("FG", "FOGGIA"),
                            ("FO", "FORLI'"),
                            ("FC", "FORLI' CESENA"),
                            ("FR", "FROSINONE"),
                            ("GE", "GENOVA"),
                            ("GO", "GORIZIA"),
                            ("GR", "GROSSETO"),
                            ("IM", "IMPERIA"),
                            ("IS", "ISERNIA"),
                            ("SP", "LA SPEZIA"),
                            ("AQ", "L'AQUILA"),
                            ("LT", "LATINA"),
                            ("LE", "LECCE"),
                            ("LC", "LECCO"),
                            ("LI", "LIVORNO"),
                            ("LO", "LODI"),
                            ("LU", "LUCCA"),
                            ("MC", "MACERATA"),
                            ("MN", "MANTOVA"),
                            ("MS", "MASSA CARRARA"),
                            ("MT", "MATERA"),
                            ("ME", "MESSINA"),
                            ("MI", "MILANO"),
                            ("MO", "MODENA"),
                            ("MB", "MONZA-BRIANZA"),
                            ("NA", "NAPOLI"),
                            ("NO", "NOVARA"),
                            ("NU", "NUORO"),
                            ("OR", "ORISTANO"),
                            ("PD", "PADOVA"),
                            ("PA", "PALERMO"),
                            ("PR", "PARMA"),
                            ("PV", "PAVIA"),
                            ("PG", "PERUGIA"),
                            ("PS", "PESARO"),
                            ("PU", "PESARO URBINO"),
                            ("PE", "PESCARA"),
                            ("PC", "PIACENZA"),
                            ("PI", "PISA"),
                            ("PT", "PISTOIA"),
                            ("PN", "PORDENONE"),
                            ("PZ", "POTENZA"),
                            ("PO", "PRATO"),
                            ("RG", "RAGUSA"),
                            ("RA", "RAVENNA"),
                            ("RC", "REGGIO CALABRIA"),
                            ("RE", "REGGIO EMILIA"),
                            ("RI", "RIETI"),
                            ("RN", "RIMINI"),
                            ("RM", "ROMA"),
                            ("RO", "ROVIGO"),
                            ("SA", "SALERNO"),
                            ("SS", "SASSARI"),
                            ("SV", "SAVONA"),
                            ("SI", "SIENA"),
                            ("SR", "SIRACUSA"),
                            ("SO", "SONDRIO"),
                            ("TA", "TARANTO"),
                            ("TE", "TERAMO"),
                            ("TR", "TERNI"),
                            ("TO", "TORINO"),
                            ("TP", "TRAPANI"),
                            ("TN", "TRENTO"),
                            ("TV", "TREVISO"),
                            ("TS", "TRIESTE"),
                            ("UD", "UDINE"),
                            ("VA", "VARESE"),
                            ("VE", "VENEZIA"),
                            ("VB", "VERBANIA"),
                            ("VC", "VERCELLI"),
                            ("VR", "VERONA"),
                            ("VV", "VIBO VALENTIA"),
                            ("VI", "VICENZA"),
                            ("VT", "VITERBO"),
                            ("EE", "Foreign State"),
                        ],
                        default="MO",
                        help_text="Italian Province where Member is born (EE for other countries)",
                        max_length=2,
                        verbose_name="Birth Province",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Phone Number, use only digits, +, -, space and parenthesis",
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^(00|\\+)?((\\d+|\\(\\d+\\))[ \\-]?)+\\d$",
                                "Use only plus sign (at start), dashes (-), spaces and parenthesis",
                            )
                        ],
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "address_description",
                    models.CharField(
                        help_text="Example: Via Roma 42/a",
                        max_length=200,
                        verbose_name="Address",
                    ),
                ),
                (
                    "address_city",
                    models.CharField(max_length=100, verbose_name="Address City"),
                ),
                (
                    "address_postal_code",
                    models.CharField(
                        max_length=5,
                        validators=[
                            django.core.validators.RegexValidator(
                                "[0-9]{5}", "Italian Postal Code is made of 5 digits"
                            )
                        ],
                        verbose_name="Postal Code",
                    ),
                ),
                (
                    "address_province",
                    models.CharField(
                        choices=[
                            ("AG", "AGRIGENTO"),
                            ("AL", "ALESSANDRIA"),
                            ("AN", "ANCONA"),
                            ("AO", "AOSTA"),
                            ("AR", "AREZZO"),
                            ("AP", "ASCOLI PICENO"),
                            ("AT", "ASTI"),
                            ("AV", "AVELLINO"),
                            ("BA", "BARI"),
                            ("BL", "BELLUNO"),
                            ("BN", "BENEVENTO"),
                            ("BG", "BERGAMO"),
                            ("BI", "BIELLA"),
                            ("BO", "BOLOGNA"),
                            ("BZ", "BOLZANO"),
                            ("BS", "BRESCIA"),
                            ("BR", "BRINDISI"),
                            ("CA", "CAGLIARI"),
                            ("CL", "CALTANISSETTA"),
                            ("CB", "CAMPOBASSO"),
                            ("CE", "CASERTA"),
                            ("CT", "CATANIA"),
                            ("CZ", "CATANZARO"),
                            ("CH", "CHIETI"),
                            ("CO", "COMO"),
                            ("CS", "COSENZA"),
                            ("CR", "CREMONA"),
                            ("KR", "CROTONE"),
                            ("CN", "CUNEO"),
                            ("EN", "ENNA"),
                            ("FM", "FERMO"),
                            ("FE", "FERRARA"),
                            ("FI", "FIRENZE"),
                            ("FG", "FOGGIA"),
                            ("FO", "FORLI'"),
                            ("FC", "FORLI' CESENA"),
                            ("FR", "FROSINONE"),
                            ("GE", "GENOVA"),
                            ("GO", "GORIZIA"),
                            ("GR", "GROSSETO"),
                            ("IM", "IMPERIA"),
                            ("IS", "ISERNIA"),
                            ("SP", "LA SPEZIA"),
                            ("AQ", "L'AQUILA"),
                            ("LT", "LATINA"),
                            ("LE", "LECCE"),
                            ("LC", "LECCO"),
                            ("LI", "LIVORNO"),
                            ("LO", "LODI"),
                            ("LU", "LUCCA"),
                            ("MC", "MACERATA"),
                            ("MN", "MANTOVA"),
                            ("MS", "MASSA CARRARA"),
                            ("MT", "MATERA"),
                            ("ME", "MESSINA"),
                            ("MI", "MILANO"),
                            ("MO", "MODENA"),
                            ("MB", "MONZA-BRIANZA"),
                            ("NA", "NAPOLI"),
                            ("NO", "NOVARA"),
                            ("NU", "NUORO"),
                            ("OR", "ORISTANO"),
                            ("PD", "PADOVA"),
                            ("PA", "PALERMO"),
                            ("PR", "PARMA"),
                            ("PV", "PAVIA"),
                            ("PG", "PERUGIA"),
                            ("PS", "PESARO"),
                            ("PU", "PESARO URBINO"),
                            ("PE", "PESCARA"),
                            ("PC", "PIACENZA"),
                            ("PI", "PISA"),
                            ("PT", "PISTOIA"),
                            ("PN", "PORDENONE"),
                            ("PZ", "POTENZA"),
                            ("PO", "PRATO"),
                            ("RG", "RAGUSA"),
                            ("RA", "RAVENNA"),
                            ("RC", "REGGIO CALABRIA"),
                            ("RE", "REGGIO EMILIA"),
                            ("RI", "RIETI"),
                            ("RN", "RIMINI"),
                            ("RM", "ROMA"),
                            ("RO", "ROVIGO"),
                            ("SA", "SALERNO"),
                            ("SS", "SASSARI"),
                            ("SV", "SAVONA"),
                            ("SI", "SIENA"),
                            ("SR", "SIRACUSA"),
                            ("SO", "SONDRIO"),
                            ("TA", "TARANTO"),
                            ("TE", "TERAMO"),
                            ("TR", "TERNI"),
                            ("TO", "TORINO"),
                            ("TP", "TRAPANI"),
                            ("TN", "TRENTO"),
                            ("TV", "TREVISO"),
                            ("TS", "TRIESTE"),
                            ("UD", "UDINE"),
                            ("VA", "VARESE"),
                            ("VE", "VENEZIA"),
                            ("VB", "VERBANIA"),
                            ("VC", "VERCELLI"),
                            ("VR", "VERONA"),
                            ("VV", "VIBO VALENTIA"),
                            ("VI", "VICENZA"),
                            ("VT", "VITERBO"),
                            ("EE", "Foreign State"),
                        ],
                        default="MO",
                        help_text="Address Province (EE for other countries)",
                        max_length=2,
                        verbose_name="Address Province",
                    ),
                ),
                (
                    "document_type",
                    models.CharField(
                        choices=[
                            ("carta-identita", "Carta Identità"),
                            ("passaporto", "Passaporto"),
                            ("patente", "Patente"),
                        ],
                        max_length=16,
                        verbose_name="Document Type",
                    ),
                ),
                (
                    "document_grant_from",
                    models.CharField(
                        help_text="Public Authority who grant you the document",
                        max_length=100,
                        verbose_name="Who has grant the Document",
                    ),
                ),
                (
                    "document_number",
                    models.CharField(
                        max_length=30, verbose_name="Document Number/Code"
                    ),
                ),
                (
                    "document_expires",
                    models.DateField(
                        default=datetime.date.today,
                        verbose_name="Document Expiration Date",
                    ),
                ),
                (
                    "privacy_acknowledgement",
                    models.DateField(
                        blank=True,
                        default=None,
                        help_text="Last date Member has read privacy page",
                        null=True,
                        verbose_name="Privacy Page Aknowledgement",
                    ),
                ),
                (
                    "profession",
                    models.CharField(
                        blank=True, default="", max_length=80, verbose_name="Profession"
                    ),
                ),
                (
                    "come_from",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=200,
                        verbose_name="How you found us",
                    ),
                ),
                (
                    "interests",
                    models.CharField(
                        blank=True, default="", max_length=200, verbose_name="Interests"
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True, default="", verbose_name="Internal Notes"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "qualification",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="members",
                        to="member.memberqualification",
                        verbose_name="Qualification",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="member",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Member",
                "verbose_name_plural": "Members",
            },
        ),
    ]
