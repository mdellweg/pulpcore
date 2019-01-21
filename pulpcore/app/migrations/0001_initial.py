# Generated by Django 2.1.4 on 2019-01-02 19:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pulpcore.app.fields
import pulpcore.app.models.content
import pulpcore.app.models.fields
import pulpcore.app.models.publication
import pulpcore.app.models.repository
import pulpcore.app.models.task
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('file', pulpcore.app.models.fields.ArtifactFileField(max_length=255, upload_to=pulpcore.app.models.content.Artifact.storage_path)),
                ('size', models.IntegerField()),
                ('md5', models.CharField(db_index=True, max_length=32)),
                ('sha1', models.CharField(db_index=True, max_length=40)),
                ('sha224', models.CharField(db_index=True, max_length=56)),
                ('sha256', models.CharField(db_index=True, max_length=64, unique=True)),
                ('sha384', models.CharField(db_index=True, max_length=96, unique=True)),
                ('sha512', models.CharField(db_index=True, max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_type', models.TextField(default=None)),
            ],
            options={
                'verbose_name_plural': 'content',
            },
            bases=(models.Model, pulpcore.app.models.content.QueryMixin),
        ),
        migrations.CreateModel(
            name='ContentArtifact',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('relative_path', models.CharField(max_length=256)),
                ('artifact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pulp_app.Artifact')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_app.Content')),
            ],
            bases=(models.Model, pulpcore.app.models.content.QueryMixin),
        ),
        migrations.CreateModel(
            name='ContentGuard',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_type', models.TextField(default=None)),
                ('name', models.CharField(db_index=True, max_length=256, unique=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CreatedResource',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('base_path', models.CharField(max_length=255, unique=True)),
                ('content_guard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distributions', to='pulp_app.ContentGuard')),
            ],
            options={
                'default_related_name': 'distributions',
            },
        ),
        migrations.CreateModel(
            name='Exporter',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_type', models.TextField(default=None)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('last_export', models.DateTimeField(null=True)),
            ],
            options={
                'default_related_name': 'exporters',
            },
        ),
        migrations.CreateModel(
            name='ProgressReport',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('message', models.TextField()),
                ('state', models.TextField(choices=[('waiting', 'Waiting'), ('skipped', 'Skipped'), ('running', 'Running'), ('completed', 'Completed'), ('failed', 'Failed'), ('canceled', 'Canceled')], default='waiting')),
                ('total', models.IntegerField(null=True)),
                ('done', models.IntegerField(default=0)),
                ('suffix', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('complete', models.BooleanField(db_index=True, default=False)),
                ('pass_through', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublishedArtifact',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('relative_path', models.CharField(max_length=255)),
                ('content_artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_artifact', to='pulp_app.ContentArtifact')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_artifact', to='pulp_app.Publication')),
            ],
            options={
                'default_related_name': 'published_artifact',
            },
        ),
        migrations.CreateModel(
            name='PublishedMetadata',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('relative_path', models.CharField(max_length=255)),
                ('file', models.FileField(max_length=255, upload_to=pulpcore.app.models.publication.PublishedMetadata._storage_path)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_metadata', to='pulp_app.Publication')),
            ],
            options={
                'default_related_name': 'published_metadata',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_type', models.TextField(default=None)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
            options={
                'default_related_name': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_type', models.TextField(default=None)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('url', models.TextField()),
                ('validate', models.BooleanField(default=True)),
                ('ssl_ca_certificate', models.FileField(max_length=255, upload_to=pulpcore.app.models.repository.Remote.tls_storage_path)),
                ('ssl_client_certificate', models.FileField(max_length=255, upload_to=pulpcore.app.models.repository.Remote.tls_storage_path)),
                ('ssl_client_key', models.FileField(max_length=255, upload_to=pulpcore.app.models.repository.Remote.tls_storage_path)),
                ('ssl_validation', models.BooleanField(default=True)),
                ('proxy_url', models.TextField()),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('download_concurrency', models.PositiveIntegerField(default=20)),
                ('policy', models.TextField(choices=[('immediate', 'When syncing, download all metadata and content now.'), ('on_demand', 'When syncing, download metadata, but do not download content now. Instead, download content as clients request it, and save it in Pulp to be served for future client requests.'), ('streamed', 'When syncing, download metadata, but do not download content now. Instead,download content as clients request it, but never save it in Pulp. This causes future requests for that same content to have to be downloaded again.')], default='immediate')),
            ],
            options={
                'default_related_name': 'remotes',
            },
        ),
        migrations.CreateModel(
            name='RemoteArtifact',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('url', models.TextField(validators=[django.core.validators.URLValidator])),
                ('size', models.IntegerField(null=True)),
                ('md5', models.CharField(max_length=32, null=True)),
                ('sha1', models.CharField(max_length=40, null=True)),
                ('sha224', models.CharField(max_length=56, null=True)),
                ('sha256', models.CharField(max_length=64, null=True)),
                ('sha384', models.CharField(max_length=96, null=True)),
                ('sha512', models.CharField(max_length=128, null=True)),
                ('content_artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_app.ContentArtifact')),
                ('remote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_app.Remote')),
            ],
            bases=(models.Model, pulpcore.app.models.content.QueryMixin),
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.TextField()),
                ('last_version', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'repositories',
            },
        ),
        migrations.CreateModel(
            name='RepositoryContent',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version_memberships', to='pulp_app.Content')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_app.Repository')),
            ],
        ),
        migrations.CreateModel(
            name='RepositoryVersion',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('number', models.PositiveIntegerField(db_index=True)),
                ('complete', models.BooleanField(db_index=True, default=False)),
                ('base_version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='versions', to='pulp_app.RepositoryVersion')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='pulp_app.Repository')),
            ],
            options={
                'ordering': ('number',),
                'get_latest_by': 'number',
                'default_related_name': 'versions',
            },
        ),
        migrations.CreateModel(
            name='ReservedResource',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('resource', models.TextField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('job_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('state', models.TextField(choices=[('waiting', 'Waiting'), ('skipped', 'Skipped'), ('running', 'Running'), ('completed', 'Completed'), ('failed', 'Failed'), ('canceled', 'Canceled')])),
                ('started_at', models.DateTimeField(null=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('non_fatal_errors', pulpcore.app.fields.JSONField(default=list)),
                ('error', pulpcore.app.fields.JSONField(null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spawned_tasks', to='pulp_app.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskReservedResource',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_app.ReservedResource')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pulp_app.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_created', models.DateTimeField(auto_now_add=True)),
                ('_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('last_heartbeat', models.DateTimeField(auto_now=True)),
                ('gracefully_stopped', models.BooleanField(default=False)),
                ('cleaned_up', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='pulp_app.Worker'),
        ),
        migrations.AddField(
            model_name='reservedresource',
            name='tasks',
            field=models.ManyToManyField(related_name='reserved_resources', through='pulp_app.TaskReservedResource', to='pulp_app.Task'),
        ),
        migrations.AddField(
            model_name='reservedresource',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='pulp_app.Worker'),
        ),
        migrations.AddField(
            model_name='repositorycontent',
            name='version_added',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_memberships', to='pulp_app.RepositoryVersion'),
        ),
        migrations.AddField(
            model_name='repositorycontent',
            name='version_removed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='removed_memberships', to='pulp_app.RepositoryVersion'),
        ),
        migrations.AddField(
            model_name='repository',
            name='content',
            field=models.ManyToManyField(related_name='repositories', through='pulp_app.RepositoryContent', to='pulp_app.Content'),
        ),
        migrations.AddField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pulp_app.Publisher'),
        ),
        migrations.AddField(
            model_name='publication',
            name='repository_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulp_app.RepositoryVersion'),
        ),
        migrations.AddField(
            model_name='progressreport',
            name='task',
            field=models.ForeignKey(default=pulpcore.app.models.task.Task.current, on_delete=django.db.models.deletion.CASCADE, related_name='progress_reports', to='pulp_app.Task'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='publication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distributions', to='pulp_app.Publication'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distributions', to='pulp_app.Publisher'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='repository',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distributions', to='pulp_app.Repository'),
        ),
        migrations.AddField(
            model_name='createdresource',
            name='task',
            field=models.ForeignKey(default=pulpcore.app.models.task.Task.current, on_delete=django.db.models.deletion.CASCADE, related_name='created_resources', to='pulp_app.Task'),
        ),
        migrations.AddField(
            model_name='content',
            name='_artifacts',
            field=models.ManyToManyField(through='pulp_app.ContentArtifact', to='pulp_app.Artifact'),
        ),
        migrations.CreateModel(
            name='ProgressBar',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('pulp_app.progressreport',),
        ),
        migrations.CreateModel(
            name='ProgressSpinner',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('pulp_app.progressreport',),
        ),
        migrations.AlterUniqueTogether(
            name='repositoryversion',
            unique_together={('repository', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='repositorycontent',
            unique_together={('repository', 'content', 'version_added'), ('repository', 'content', 'version_removed')},
        ),
        migrations.AlterUniqueTogether(
            name='remoteartifact',
            unique_together={('content_artifact', 'remote')},
        ),
        migrations.AlterUniqueTogether(
            name='publishedmetadata',
            unique_together={('publication', 'relative_path'), ('publication', 'file')},
        ),
        migrations.AlterUniqueTogether(
            name='publishedartifact',
            unique_together={('publication', 'relative_path'), ('publication', 'content_artifact')},
        ),
        migrations.AlterUniqueTogether(
            name='contentartifact',
            unique_together={('content', 'relative_path')},
        ),
    ]