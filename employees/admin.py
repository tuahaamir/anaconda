from django.contrib import admin
from . import models
from django.db.models import Q
import random


class AttendanceInline(admin.TabularInline):
    model = models.Attendance
    extra = 0
    list_display = ["employee", "get_date", "check_in", "check_out"]

    def __init__(self, *args, **kwargs):
        month = kwargs.pop("month")
        year = kwargs.pop("year")
        self.user_id = kwargs.pop("user_id")
        self.verbose_name = f"{month} {year}"
        self.month = month
        self.year = year
        super().__init__(*args, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(
            Q(employee__id=self.user_id) & Q(date__month=self.month) & Q(date__year=self.year)
        )
        return queryset


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
    def get_inline_instances(self, request, obj=None):
        user_id = obj.id
        inline_instances = []
        for year in [2023, 2024]:
            for month in range(1, 13):
                inline = AttendanceInline(
                    self.model, self.admin_site, user_id=user_id, month=month, year=year
                )
                if inline.get_queryset(request):
                    inline_instances.append(inline)
        return inline_instances


@admin.register(models.EmployeeDetails)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Skills)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EmployeeFinance)
class FinanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Holiday)
class HolidayAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["employee", "date", "check_in", "check_out"]


# @admin.register(models.Attendance)
# class AttendanceAdmin(admin.ModelAdmin):
#     pass

@admin.register(models.EmployeeSkills)
class EmployeeSkillsAdmin(admin.ModelAdmin):
    pass