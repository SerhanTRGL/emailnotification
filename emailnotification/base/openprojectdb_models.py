# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    show_until = models.DateField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcements'


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True)
    value = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class AttachableJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    journal_id = models.BigIntegerField()
    attachment_id = models.BigIntegerField()
    filename = models.CharField()

    class Meta:
        managed = False
        db_table = 'attachable_journals'


class AttachmentJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    container_id = models.BigIntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=30, blank=True, null=True)
    filename = models.CharField()
    disk_filename = models.CharField()
    filesize = models.BigIntegerField()
    content_type = models.CharField(blank=True, null=True)
    digest = models.CharField(max_length=40)
    downloads = models.IntegerField()
    author_id = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment_journals'


class Attachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    container_id = models.BigIntegerField(blank=True, null=True)
    container_type = models.CharField(max_length=30, blank=True, null=True)
    filename = models.CharField()
    disk_filename = models.CharField()
    filesize = models.BigIntegerField()
    content_type = models.CharField(blank=True, null=True)
    digest = models.CharField(max_length=40)
    downloads = models.IntegerField()
    author_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    file = models.CharField(blank=True, null=True)
    fulltext = models.TextField(blank=True, null=True)
    fulltext_tsv = models.TextField(blank=True, null=True)  # This field type is a guess.
    file_tsv = models.TextField(blank=True, null=True)  # This field type is a guess.
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class AttributeHelpTexts(models.Model):
    id = models.BigAutoField(primary_key=True)
    help_text = models.TextField()
    type = models.CharField()
    attribute_name = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attribute_help_texts'


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


class BcfComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.TextField(blank=True, null=True)
    journal_id = models.BigIntegerField(blank=True, null=True)
    issue = models.ForeignKey('BcfIssues', models.DO_NOTHING, blank=True, null=True)
    viewpoint = models.ForeignKey('BcfViewpoints', models.DO_NOTHING, blank=True, null=True)
    reply_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reply_to', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bcf_comments'
        unique_together = (('uuid', 'issue'),)


class BcfIssues(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.TextField(unique=True, blank=True, null=True)
    markup = models.TextField(blank=True, null=True)  # This field type is a guess.
    work_package = models.OneToOneField('WorkPackages', models.DO_NOTHING, blank=True, null=True)
    stage = models.CharField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    labels = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bcf_issues'


class BcfViewpoints(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.TextField(blank=True, null=True)
    viewpoint_name = models.TextField(blank=True, null=True)
    issue = models.ForeignKey(BcfIssues, models.DO_NOTHING, blank=True, null=True)
    json_viewpoint = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bcf_viewpoints'
        unique_together = (('uuid', 'issue'),)


class BudgetJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    subject = models.CharField()
    description = models.TextField(blank=True, null=True)
    fixed_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'budget_journals'


class Budgets(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    subject = models.CharField()
    description = models.TextField()
    fixed_date = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budgets'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    name = models.CharField()
    assigned_to_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class Changes(models.Model):
    id = models.BigAutoField(primary_key=True)
    changeset_id = models.BigIntegerField()
    action = models.CharField(max_length=1)
    path = models.TextField()
    from_path = models.TextField(blank=True, null=True)
    from_revision = models.CharField(blank=True, null=True)
    revision = models.CharField(blank=True, null=True)
    branch = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changes'


class ChangesetJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    repository_id = models.BigIntegerField()
    revision = models.CharField()
    committer = models.CharField(blank=True, null=True)
    committed_on = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    commit_date = models.DateField(blank=True, null=True)
    scmid = models.CharField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changeset_journals'


class Changesets(models.Model):
    id = models.BigAutoField(primary_key=True)
    repository_id = models.BigIntegerField()
    revision = models.CharField()
    committer = models.CharField(blank=True, null=True)
    committed_on = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    commit_date = models.DateField(blank=True, null=True)
    scmid = models.CharField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changesets'
        unique_together = (('repository_id', 'revision'),)


class ChangesetsWorkPackages(models.Model):
    changeset_id = models.BigIntegerField()
    work_package_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'changesets_work_packages'
        unique_together = (('changeset_id', 'work_package_id'),)


class Colors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    hexcode = models.CharField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colors'


class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    commented_type = models.CharField(max_length=30)
    commented_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class CostEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    project_id = models.BigIntegerField()
    work_package_id = models.BigIntegerField()
    cost_type_id = models.BigIntegerField()
    units = models.FloatField()
    spent_on = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comments = models.CharField()
    blocked = models.BooleanField()
    overridden_costs = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    costs = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    rate_id = models.BigIntegerField(blank=True, null=True)
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    logged_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_entries'


class CostQueries(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    project_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField()
    is_public = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    serialized = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'cost_queries'


class CostTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    unit = models.CharField()
    unit_plural = models.CharField()
    default = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_types'


class CustomActions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    actions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_actions'


class CustomActionsProjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    custom_action_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_actions_projects'


class CustomActionsRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.BigIntegerField(blank=True, null=True)
    custom_action_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_actions_roles'


class CustomActionsStatuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_id = models.BigIntegerField(blank=True, null=True)
    custom_action_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_actions_statuses'


class CustomActionsTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_id = models.BigIntegerField(blank=True, null=True)
    custom_action_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_actions_types'


class CustomFields(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=30)
    field_format = models.CharField(max_length=30)
    regexp = models.CharField(blank=True, null=True)
    min_length = models.IntegerField()
    max_length = models.IntegerField()
    is_required = models.BooleanField()
    is_for_all = models.BooleanField()
    is_filter = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    searchable = models.BooleanField(blank=True, null=True)
    editable = models.BooleanField(blank=True, null=True)
    visible = models.BooleanField()
    multi_value = models.BooleanField(blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    content_right_to_left = models.BooleanField(blank=True, null=True)
    allow_non_open_versions = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_fields'


class CustomFieldsProjects(models.Model):
    custom_field = models.ForeignKey(CustomFields, models.DO_NOTHING)
    project = models.ForeignKey('Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'custom_fields_projects'
        unique_together = (('custom_field', 'project'),)


class CustomFieldsTypes(models.Model):
    custom_field_id = models.BigIntegerField()
    type_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields_types'
        unique_together = (('custom_field_id', 'type_id'),)


class CustomOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    custom_field_id = models.BigIntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    default_value = models.BooleanField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_options'


class CustomStyles(models.Model):
    id = models.BigAutoField(primary_key=True)
    logo = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    favicon = models.CharField(blank=True, null=True)
    touch_icon = models.CharField(blank=True, null=True)
    theme = models.CharField(blank=True, null=True)
    theme_logo = models.CharField(blank=True, null=True)
    export_logo = models.CharField(blank=True, null=True)
    export_cover = models.CharField(blank=True, null=True)
    export_cover_text_color = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_styles'


class CustomValues(models.Model):
    id = models.BigAutoField(primary_key=True)
    customized_type = models.CharField(max_length=30)
    customized_id = models.BigIntegerField()
    custom_field_id = models.BigIntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_values'


class CustomizableJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    journal_id = models.BigIntegerField()
    custom_field_id = models.BigIntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customizable_journals'


class DelayedJobStatuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference_type = models.CharField(blank=True, null=True)
    reference_id = models.BigIntegerField(blank=True, null=True)
    message = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_id = models.BigIntegerField(blank=True, null=True)
    job_id = models.CharField(unique=True, blank=True, null=True)
    payload = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delayed_job_statuses'
        unique_together = (('reference_type', 'reference_id'),)


class DelayedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    priority = models.IntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    handler = models.TextField(blank=True, null=True)
    last_error = models.TextField(blank=True, null=True)
    run_at = models.DateTimeField(blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    failed_at = models.DateTimeField(blank=True, null=True)
    locked_by = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    queue = models.CharField(blank=True, null=True)
    cron = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delayed_jobs'


class DesignColors(models.Model):
    id = models.BigAutoField(primary_key=True)
    variable = models.CharField(unique=True, blank=True, null=True)
    hexcode = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'design_colors'


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


class DocumentJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    category_id = models.BigIntegerField()
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_journals'


class Documents(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    category_id = models.BigIntegerField()
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class DoneStatusesForProject(models.Model):
    project_id = models.BigIntegerField(blank=True, null=True)
    status_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'done_statuses_for_project'


class EnabledModules(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'enabled_modules'


class EnterpriseTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    encoded_token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'enterprise_tokens'


class Enumerations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    position = models.IntegerField(blank=True, null=True)
    is_default = models.BooleanField()
    type = models.CharField(blank=True, null=True)
    active = models.BooleanField()
    project_id = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    color_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enumerations'


class Exports(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exports'


class FileLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    storage = models.ForeignKey('Storages', models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING)
    container_id = models.BigIntegerField(blank=True, null=True)
    container_type = models.CharField(blank=True, null=True)
    origin_id = models.CharField(blank=True, null=True)
    origin_name = models.CharField(blank=True, null=True)
    origin_created_by_name = models.CharField(blank=True, null=True)
    origin_last_modified_by_name = models.CharField(blank=True, null=True)
    origin_mime_type = models.CharField(blank=True, null=True)
    origin_created_at = models.DateTimeField(blank=True, null=True)
    origin_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'file_links'


class Forums(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    name = models.CharField()
    description = models.CharField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    topics_count = models.IntegerField()
    messages_count = models.IntegerField()
    last_message_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forums'


class GithubCheckRuns(models.Model):
    id = models.BigAutoField(primary_key=True)
    github_pull_request_id = models.BigIntegerField()
    github_id = models.BigIntegerField()
    github_html_url = models.CharField()
    app_id = models.BigIntegerField()
    github_app_owner_avatar_url = models.CharField()
    status = models.CharField()
    name = models.CharField()
    conclusion = models.CharField(blank=True, null=True)
    output_title = models.CharField(blank=True, null=True)
    output_summary = models.CharField(blank=True, null=True)
    details_url = models.CharField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'github_check_runs'


class GithubPullRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    github_user_id = models.BigIntegerField(blank=True, null=True)
    merged_by_id = models.BigIntegerField(blank=True, null=True)
    github_id = models.BigIntegerField(blank=True, null=True)
    number = models.IntegerField()
    github_html_url = models.CharField()
    state = models.CharField()
    repository = models.CharField()
    github_updated_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    draft = models.BooleanField(blank=True, null=True)
    merged = models.BooleanField(blank=True, null=True)
    merged_at = models.DateTimeField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)
    review_comments_count = models.IntegerField(blank=True, null=True)
    additions_count = models.IntegerField(blank=True, null=True)
    deletions_count = models.IntegerField(blank=True, null=True)
    changed_files_count = models.IntegerField(blank=True, null=True)
    labels = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    repository_html_url = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'github_pull_requests'


class GithubPullRequestsWorkPackages(models.Model):
    github_pull_request_id = models.BigIntegerField()
    work_package_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'github_pull_requests_work_packages'
        unique_together = (('github_pull_request_id', 'work_package_id'),)


class GithubUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    github_id = models.BigIntegerField()
    github_login = models.CharField()
    github_html_url = models.CharField()
    github_avatar_url = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'github_users'


class GridWidgets(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_row = models.IntegerField()
    end_row = models.IntegerField()
    start_column = models.IntegerField()
    end_column = models.IntegerField()
    identifier = models.CharField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    grid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grid_widgets'


class Grids(models.Model):
    id = models.BigAutoField(primary_key=True)
    row_count = models.IntegerField()
    column_count = models.IntegerField()
    type = models.CharField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    project_id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grids'


class GroupUsers(models.Model):
    group_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'group_users'
        unique_together = (('group_id', 'user_id'), ('user_id', 'group_id'),)


class IcalTokenQueryAssignments(models.Model):
    id = models.BigAutoField(primary_key=True)
    ical_token = models.ForeignKey('Tokens', models.DO_NOTHING, blank=True, null=True)
    query = models.ForeignKey('Queries', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'ical_token_query_assignments'


class IfcModels(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    uploader_id = models.BigIntegerField(blank=True, null=True)
    is_default = models.BooleanField()
    conversion_status = models.IntegerField(blank=True, null=True)
    conversion_error_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifc_models'


class Journals(models.Model):
    id = models.BigAutoField(primary_key=True)
    journable_type = models.CharField(blank=True, null=True)
    journable_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    version = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    data_type = models.CharField()
    data_id = models.BigIntegerField()
    cause = models.JSONField(blank=True, null=True)
    validity_period = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'journals'
        unique_together = (('data_id', 'data_type'), ('journable_type', 'journable_id', 'version'),)


class LaborBudgetItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    budget_id = models.BigIntegerField()
    hours = models.FloatField()
    user_id = models.BigIntegerField(blank=True, null=True)
    comments = models.CharField()
    amount = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_budget_items'


class LastProjectFolders(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_storage = models.ForeignKey('ProjectStorages', models.DO_NOTHING)
    origin_folder_id = models.CharField(blank=True, null=True)
    mode = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'last_project_folders'
        unique_together = (('project_storage', 'mode'),)
        db_table_comment = 'This table contains the last used project folder IDs for a project storage per mode.'


class LdapAuthSources(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    host = models.CharField(max_length=60, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    account = models.CharField(blank=True, null=True)
    account_password = models.CharField(blank=True, null=True)
    base_dn = models.CharField(blank=True, null=True)
    attr_login = models.CharField(max_length=30, blank=True, null=True)
    attr_firstname = models.CharField(max_length=30, blank=True, null=True)
    attr_lastname = models.CharField(max_length=30, blank=True, null=True)
    attr_mail = models.CharField(max_length=30, blank=True, null=True)
    onthefly_register = models.BooleanField()
    attr_admin = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tls_mode = models.IntegerField()
    filter_string = models.TextField(blank=True, null=True)
    verify_peer = models.BooleanField()
    tls_certificate_string = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ldap_auth_sources'


class LdapGroupsMemberships(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ldap_groups_memberships'
        unique_together = (('user_id', 'group_id'),)


class LdapGroupsSynchronizedFilters(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    group_name_attribute = models.CharField(blank=True, null=True)
    filter_string = models.CharField(blank=True, null=True)
    ldap_auth_source_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    base_dn = models.TextField(blank=True, null=True)
    sync_users = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ldap_groups_synchronized_filters'


class LdapGroupsSynchronizedGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    ldap_auth_source_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    dn = models.TextField(blank=True, null=True)
    users_count = models.IntegerField()
    filter = models.ForeignKey(LdapGroupsSynchronizedFilters, models.DO_NOTHING, blank=True, null=True)
    sync_users = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ldap_groups_synchronized_groups'


class MaterialBudgetItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    budget_id = models.BigIntegerField()
    units = models.FloatField()
    cost_type_id = models.BigIntegerField(blank=True, null=True)
    comments = models.CharField()
    amount = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_budget_items'


class MeetingAgendaItemJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    journal_id = models.IntegerField(blank=True, null=True)
    agenda_item_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    duration_in_minutes = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    work_package_id = models.IntegerField(blank=True, null=True)
    item_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_agenda_item_journals'


class MeetingAgendaItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    meeting = models.ForeignKey('Meetings', models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    duration_in_minutes = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    work_package_id = models.BigIntegerField(blank=True, null=True)
    item_type = models.SmallIntegerField(blank=True, null=True)
    lock_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meeting_agenda_items'


class MeetingContentJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    meeting_id = models.BigIntegerField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    locked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_content_journals'


class MeetingContents(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(blank=True, null=True)
    meeting_id = models.BigIntegerField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    lock_version = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    locked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_contents'


class MeetingJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_journals'


class MeetingParticipants(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    meeting_id = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    invited = models.BooleanField(blank=True, null=True)
    attended = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'meeting_participants'


class Meetings(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    state = models.IntegerField()
    type = models.CharField()
    lock_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meetings'


class MemberRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    member_id = models.BigIntegerField()
    role_id = models.BigIntegerField()
    inherited_from = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_roles'
        unique_together = (('member_id', 'role_id', 'inherited_from'),)


class Members(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    project_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    entity_type = models.CharField(blank=True, null=True)
    entity_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'
        unique_together = (('user_id', 'project_id', 'entity_type', 'entity_id'), ('user_id', 'project_id'),)


class MenuItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    navigatable_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_items'


class MessageJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    forum_id = models.BigIntegerField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    subject = models.CharField()
    content = models.TextField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    locked = models.BooleanField(blank=True, null=True)
    sticky = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_journals'


class Messages(models.Model):
    id = models.BigAutoField(primary_key=True)
    forum_id = models.BigIntegerField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    subject = models.CharField()
    content = models.TextField(blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    replies_count = models.IntegerField()
    last_reply_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    locked = models.BooleanField(blank=True, null=True)
    sticky = models.IntegerField(blank=True, null=True)
    sticked_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    title = models.CharField()
    summary = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    comments_count = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class NewsJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    title = models.CharField()
    summary = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author_id = models.BigIntegerField()
    comments_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news_journals'


class NonWorkingDays(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    date = models.DateField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'non_working_days'


class NotificationSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    watched = models.BooleanField(blank=True, null=True)
    mentioned = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    work_package_commented = models.BooleanField(blank=True, null=True)
    work_package_created = models.BooleanField(blank=True, null=True)
    work_package_processed = models.BooleanField(blank=True, null=True)
    work_package_prioritized = models.BooleanField(blank=True, null=True)
    work_package_scheduled = models.BooleanField(blank=True, null=True)
    news_added = models.BooleanField(blank=True, null=True)
    news_commented = models.BooleanField(blank=True, null=True)
    document_added = models.BooleanField(blank=True, null=True)
    forum_messages = models.BooleanField(blank=True, null=True)
    wiki_page_added = models.BooleanField(blank=True, null=True)
    wiki_page_updated = models.BooleanField(blank=True, null=True)
    membership_added = models.BooleanField(blank=True, null=True)
    membership_updated = models.BooleanField(blank=True, null=True)
    start_date = models.IntegerField(blank=True, null=True)
    due_date = models.IntegerField(blank=True, null=True)
    overdue = models.IntegerField(blank=True, null=True)
    assignee = models.BooleanField()
    responsible = models.BooleanField()
    shared = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'notification_settings'
        unique_together = (('user', 'project'),)


class Notifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.TextField(blank=True, null=True)
    read_ian = models.BooleanField(blank=True, null=True)
    reason = models.SmallIntegerField(blank=True, null=True)
    recipient = models.ForeignKey('Users', models.DO_NOTHING)
    actor = models.ForeignKey('Users', models.DO_NOTHING, related_name='notifications_actor_set', blank=True, null=True)
    resource_type = models.CharField()
    resource_id = models.BigIntegerField()
    project_id = models.BigIntegerField(blank=True, null=True)
    journal = models.ForeignKey(Journals, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    mail_reminder_sent = models.BooleanField(blank=True, null=True)
    mail_alert_sent = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OauthAccessGrants(models.Model):
    id = models.BigAutoField(primary_key=True)
    resource_owner_id = models.BigIntegerField()
    application = models.ForeignKey('OauthApplications', models.DO_NOTHING)
    token = models.CharField(unique=True)
    expires_in = models.IntegerField()
    redirect_uri = models.TextField()
    created_at = models.DateTimeField()
    revoked_at = models.DateTimeField(blank=True, null=True)
    scopes = models.CharField(blank=True, null=True)
    code_challenge = models.CharField(blank=True, null=True)
    code_challenge_method = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_grants'


class OauthAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    resource_owner_id = models.BigIntegerField(blank=True, null=True)
    application = models.ForeignKey('OauthApplications', models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(unique=True)
    refresh_token = models.CharField(unique=True, blank=True, null=True)
    expires_in = models.IntegerField(blank=True, null=True)
    revoked_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    scopes = models.CharField(blank=True, null=True)
    previous_refresh_token = models.CharField()

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthApplications(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    uid = models.CharField(unique=True)
    secret = models.CharField()
    owner_type = models.CharField(blank=True, null=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    client_credentials_user = models.ForeignKey('Users', models.DO_NOTHING, related_name='oauthapplications_client_credentials_user_set', blank=True, null=True)
    redirect_uri = models.TextField()
    scopes = models.CharField()
    confidential = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    integration_type = models.CharField(blank=True, null=True)
    integration_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_applications'


class OauthClientTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauth_client = models.ForeignKey('OauthClients', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    access_token = models.CharField(blank=True, null=True)
    refresh_token = models.CharField(blank=True, null=True)
    token_type = models.CharField(blank=True, null=True)
    expires_in = models.IntegerField(blank=True, null=True)
    scope = models.CharField(blank=True, null=True)
    origin_user_id = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth_client_tokens'
        unique_together = (('user', 'oauth_client'),)


class OauthClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.CharField()
    client_secret = models.CharField(blank=True, null=True)
    integration_type = models.CharField()
    integration_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth_clients'
        unique_together = (('integration_type', 'integration_id'),)


class OidcUserSessionLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    oidc_session = models.CharField()
    session = models.ForeignKey('Sessions', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oidc_user_session_links'


class OrderedWorkPackages(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.IntegerField()
    query = models.ForeignKey('Queries', models.DO_NOTHING, blank=True, null=True)
    work_package = models.ForeignKey('WorkPackages', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordered_work_packages'


class PaperTrailAudits(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_type = models.CharField()
    item_id = models.BigIntegerField()
    event = models.CharField()
    whodunnit = models.CharField(blank=True, null=True)
    stack = models.TextField(blank=True, null=True)
    object = models.JSONField(blank=True, null=True)
    object_changes = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper_trail_audits'


class ProjectJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    public = models.BooleanField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    identifier = models.CharField()
    active = models.BooleanField()
    templated = models.BooleanField()
    status_code = models.IntegerField(blank=True, null=True)
    status_explanation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_journals'


class ProjectQueries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    user_id = models.BigIntegerField()
    filters = models.TextField(blank=True, null=True)  # This field type is a guess.
    columns = models.TextField(blank=True, null=True)  # This field type is a guess.
    orders = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_queries'


class ProjectStorages(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)
    storage = models.ForeignKey('Storages', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    project_folder_id = models.CharField(blank=True, null=True)
    project_folder_mode = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'project_storages'
        unique_together = (('project', 'storage'),)


class Projects(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    public = models.BooleanField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(unique=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    active = models.BooleanField()
    templated = models.BooleanField()
    status_code = models.IntegerField(blank=True, null=True)
    status_explanation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class ProjectsTypes(models.Model):
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    type = models.ForeignKey('Types', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_types'
        unique_together = (('project', 'type'),)


class Queries(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField()
    filters = models.TextField(blank=True, null=True)
    user_id = models.BigIntegerField()
    public = models.BooleanField()
    column_names = models.TextField(blank=True, null=True)
    sort_criteria = models.TextField(blank=True, null=True)
    group_by = models.CharField(blank=True, null=True)
    display_sums = models.BooleanField()
    timeline_visible = models.BooleanField(blank=True, null=True)
    show_hierarchies = models.BooleanField(blank=True, null=True)
    timeline_zoom_level = models.IntegerField(blank=True, null=True)
    timeline_labels = models.TextField(blank=True, null=True)
    highlighting_mode = models.TextField(blank=True, null=True)
    highlighted_attributes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    display_representation = models.TextField(blank=True, null=True)
    starred = models.BooleanField(blank=True, null=True)
    include_subprojects = models.BooleanField()
    timestamps = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queries'


class Rates(models.Model):
    id = models.BigAutoField(primary_key=True)
    valid_from = models.DateField()
    rate = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField()
    project_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    cost_type_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rates'


class RecaptchaEntries(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recaptcha_entries'


class Relations(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    delay = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    relation_type = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relations'
        unique_together = (('from_id', 'to_id', 'relation_type'), ('to_id', 'from_id', 'relation_type'),)


class Repositories(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    url = models.CharField()
    login = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(blank=True, null=True)
    root_url = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    path_encoding = models.CharField(max_length=64, blank=True, null=True)
    log_encoding = models.CharField(max_length=64, blank=True, null=True)
    scm_type = models.CharField()
    required_storage_bytes = models.BigIntegerField()
    storage_updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repositories'


class RolePermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.CharField(blank=True, null=True)
    role_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'role_permissions'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    position = models.IntegerField(blank=True, null=True)
    builtin = models.IntegerField()
    type = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Sessions(models.Model):
    id = models.BigAutoField(primary_key=True)
    session_id = models.CharField()
    data = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Settings(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    value = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class Statuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    is_closed = models.BooleanField()
    is_default = models.BooleanField()
    position = models.IntegerField(blank=True, null=True)
    default_done_ratio = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    color_id = models.BigIntegerField(blank=True, null=True)
    is_readonly = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statuses'


class Storages(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider_type = models.CharField()
    name = models.CharField(unique=True)
    host = models.CharField(unique=True, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    provider_fields = models.JSONField()
    health_status = models.TextField()  # This field type is a guess.
    health_changed_at = models.DateTimeField()
    health_reason = models.CharField(blank=True, null=True)
    health_checked_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'storages'


class StoragesFileLinksJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    journal = models.ForeignKey(Journals, models.DO_NOTHING)
    file_link_id = models.BigIntegerField()
    link_name = models.CharField()
    storage_name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storages_file_links_journals'


class TimeEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    work_package_id = models.BigIntegerField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    comments = models.CharField(blank=True, null=True)
    activity_id = models.BigIntegerField(blank=True, null=True)
    spent_on = models.DateField()
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    overridden_costs = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    costs = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    rate_id = models.BigIntegerField(blank=True, null=True)
    logged_by = models.ForeignKey('Users', models.DO_NOTHING)
    ongoing = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'time_entries'
        unique_together = (('user_id', 'ongoing'),)


class TimeEntryActivitiesProjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    activity = models.ForeignKey(Enumerations, models.DO_NOTHING)
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_entry_activities_projects'
        unique_together = (('project', 'activity'),)


class TimeEntryJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    work_package_id = models.BigIntegerField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    comments = models.CharField(blank=True, null=True)
    activity_id = models.BigIntegerField(blank=True, null=True)
    spent_on = models.DateField()
    tyear = models.IntegerField()
    tmonth = models.IntegerField()
    tweek = models.IntegerField()
    overridden_costs = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    costs = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rate_id = models.BigIntegerField(blank=True, null=True)
    logged_by = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'time_entry_journals'


class Tokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    value = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    expires_on = models.DateTimeField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tokens'


class TwoFactorAuthenticationDevices(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(blank=True, null=True)
    default = models.BooleanField()
    active = models.BooleanField()
    channel = models.CharField()
    phone_number = models.CharField(blank=True, null=True)
    identifier = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    last_used_at = models.IntegerField(blank=True, null=True)
    otp_secret = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'two_factor_authentication_devices'


class Types(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    position = models.IntegerField(blank=True, null=True)
    is_in_roadmap = models.BooleanField()
    is_milestone = models.BooleanField()
    is_default = models.BooleanField()
    color = models.ForeignKey(Colors, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_standard = models.BooleanField()
    attribute_groups = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class UserPasswords(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    hashed_password = models.CharField(max_length=128)
    salt = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField()

    class Meta:
        managed = False
        db_table = 'user_passwords'


class UserPreferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    settings = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_preferences'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=256)
    firstname = models.CharField()
    lastname = models.CharField()
    mail = models.CharField()
    admin = models.BooleanField()
    status = models.IntegerField()
    last_login_on = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=5, blank=True, null=True)
    ldap_auth_source_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    identity_url = models.CharField(blank=True, null=True)
    first_login = models.BooleanField()
    force_password_change = models.BooleanField(blank=True, null=True)
    failed_login_count = models.IntegerField(blank=True, null=True)
    last_failed_login_on = models.DateTimeField(blank=True, null=True)
    consented_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('lastname', 'type'),)


class VersionSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    version_id = models.BigIntegerField(blank=True, null=True)
    display = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'version_settings'


class Versions(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    name = models.CharField()
    description = models.CharField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    wiki_page_title = models.CharField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    sharing = models.CharField()
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versions'


class Views(models.Model):
    id = models.BigAutoField(primary_key=True)
    query = models.OneToOneField(Queries, models.DO_NOTHING)
    options = models.JSONField()
    type = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'views'


class Watchers(models.Model):
    id = models.BigAutoField(primary_key=True)
    watchable_type = models.CharField()
    watchable_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watchers'


class WebhooksEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    webhooks_webhook = models.ForeignKey('WebhooksWebhooks', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webhooks_events'


class WebhooksLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    webhooks_webhook = models.ForeignKey('WebhooksWebhooks', models.DO_NOTHING, blank=True, null=True)
    event_name = models.CharField(blank=True, null=True)
    url = models.CharField(blank=True, null=True)
    request_headers = models.TextField(blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)
    response_headers = models.TextField(blank=True, null=True)
    response_body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'webhooks_logs'


class WebhooksProjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
    webhooks_webhook = models.ForeignKey('WebhooksWebhooks', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webhooks_projects'


class WebhooksWebhooks(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    description = models.TextField()
    secret = models.CharField(blank=True, null=True)
    enabled = models.BooleanField()
    all_projects = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'webhooks_webhooks'


class WikiPageJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wiki_page_journals'


class WikiPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    wiki_id = models.BigIntegerField()
    title = models.CharField()
    created_at = models.DateTimeField()
    protected = models.BooleanField()
    parent_id = models.BigIntegerField(blank=True, null=True)
    slug = models.CharField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(Users, models.DO_NOTHING)
    text = models.TextField(blank=True, null=True)
    lock_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wiki_pages'
        unique_together = (('wiki_id', 'slug'),)


class WikiRedirects(models.Model):
    id = models.BigAutoField(primary_key=True)
    wiki_id = models.BigIntegerField()
    title = models.CharField(blank=True, null=True)
    redirects_to = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wiki_redirects'


class Wikis(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    start_page = models.CharField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wikis'


class WorkPackageHierarchies(models.Model):
    ancestor_id = models.IntegerField()
    descendant_id = models.IntegerField()
    generations = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'work_package_hierarchies'
        unique_together = (('ancestor_id', 'descendant_id', 'generations'),)


class WorkPackageJournals(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_id = models.BigIntegerField()
    project_id = models.BigIntegerField()
    subject = models.CharField()
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    status_id = models.BigIntegerField()
    assigned_to_id = models.BigIntegerField(blank=True, null=True)
    priority_id = models.BigIntegerField()
    version_id = models.BigIntegerField(blank=True, null=True)
    author_id = models.BigIntegerField()
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    responsible_id = models.BigIntegerField(blank=True, null=True)
    budget_id = models.BigIntegerField(blank=True, null=True)
    story_points = models.IntegerField(blank=True, null=True)
    remaining_hours = models.FloatField(blank=True, null=True)
    derived_estimated_hours = models.FloatField(blank=True, null=True)
    schedule_manually = models.BooleanField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    ignore_non_working_days = models.BooleanField()
    derived_remaining_hours = models.FloatField(blank=True, null=True)
    derived_done_ratio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_package_journals'


class WorkPackages(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(Types, models.DO_NOTHING)
    project = models.ForeignKey(Projects, models.DO_NOTHING)
    subject = models.CharField()
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    status = models.ForeignKey(Statuses, models.DO_NOTHING)
    assigned_to_id = models.BigIntegerField(blank=True, null=True)
    priority_id = models.BigIntegerField(blank=True, null=True)
    version_id = models.BigIntegerField(blank=True, null=True)
    author_id = models.BigIntegerField()
    lock_version = models.IntegerField()
    done_ratio = models.IntegerField()
    estimated_hours = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    responsible_id = models.BigIntegerField(blank=True, null=True)
    budget_id = models.BigIntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    story_points = models.IntegerField(blank=True, null=True)
    remaining_hours = models.FloatField(blank=True, null=True)
    derived_estimated_hours = models.FloatField(blank=True, null=True)
    schedule_manually = models.BooleanField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    ignore_non_working_days = models.BooleanField()
    derived_remaining_hours = models.FloatField(blank=True, null=True)
    derived_done_ratio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_packages'


class Workflows(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(Types, models.DO_NOTHING)
    old_status = models.ForeignKey(Statuses, models.DO_NOTHING)
    new_status = models.ForeignKey(Statuses, models.DO_NOTHING, related_name='workflows_new_status_set')
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    assignee = models.BooleanField()
    author = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'workflows'
