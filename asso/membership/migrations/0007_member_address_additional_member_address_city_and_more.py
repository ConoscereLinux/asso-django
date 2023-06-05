# Generated by Django 4.2.1 on 2023-06-05 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("membership", "0006_member_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="address_additional",
            field=models.CharField(
                blank=True,
                default="",
                max_length=150,
                verbose_name="Address additional info",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="address_city",
            field=models.CharField(
                default="INVALID", max_length=100, verbose_name="Address City"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="address_description",
            field=models.CharField(
                default="INVALID", max_length=150, verbose_name="Address description"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="address_number",
            field=models.CharField(
                default="INVALID", max_length=8, verbose_name="Address Number"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="address_postal_code",
            field=models.CharField(
                default="00000",
                max_length=5,
                validators=[
                    django.core.validators.RegexValidator(
                        "[0-9]{5}", "Italian Postal Code is made of 5 digits"
                    )
                ],
                verbose_name="Postal Code",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="address_province",
            field=models.CharField(
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
        migrations.AlterField(
            model_name="member",
            name="birth_province",
            field=models.CharField(
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
    ]