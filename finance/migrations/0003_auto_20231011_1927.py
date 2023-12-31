# Generated by Django 3.2.22 on 2023-10-11 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='date',
            name='real_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Реальная сумма на указанную дату'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='custom_replay_days',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество дней повторения для кастомного повтора'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='finish_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания повтора'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='replay_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.replaytype'),
        ),
        migrations.AlterField(
            model_name='profit',
            name='custom_replay_days',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество дней повторения для кастомного повтора'),
        ),
        migrations.AlterField(
            model_name='profit',
            name='finish_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания повтора'),
        ),
        migrations.AlterField(
            model_name='profit',
            name='replay_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.replaytype'),
        ),
        migrations.AlterField(
            model_name='replaytype',
            name='days',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество дней повторения'),
        ),
        migrations.AlterField(
            model_name='replaytype',
            name='month',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество месяцев повторения'),
        ),
        migrations.AlterField(
            model_name='replaytype',
            name='years',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество лет повторения'),
        ),
    ]
