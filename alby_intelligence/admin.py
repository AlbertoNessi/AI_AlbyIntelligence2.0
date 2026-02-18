from django.contrib import admin

from .models import Users, Files, CCNL, ContractTypes, Contracts, Roles, Section, RoleSections, Employees

admin.site.register(Users)
admin.site.register(Files)
admin.site.register(CCNL)
admin.site.register(ContractTypes)
admin.site.register(Contracts)
admin.site.register(Roles)
admin.site.register(Section)
admin.site.register(RoleSections)
admin.site.register(Employees)
