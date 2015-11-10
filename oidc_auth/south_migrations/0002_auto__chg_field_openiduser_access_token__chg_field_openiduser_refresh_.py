# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'OpenIDUser.access_token'
        db.alter_column('oidc_auth_openiduser', 'access_token', self.gf('django.db.models.fields.CharField')(max_length=1500))

        # Changing field 'OpenIDUser.refresh_token'
        db.alter_column('oidc_auth_openiduser', 'refresh_token', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'Nonce.redirect_url'
        db.alter_column('oidc_auth_nonce', 'redirect_url', self.gf('django.db.models.fields.CharField')(max_length=1000))


    def backwards(self, orm):
        
        # Changing field 'OpenIDUser.access_token'
        db.alter_column('oidc_auth_openiduser', 'access_token', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'OpenIDUser.refresh_token'
        db.alter_column('oidc_auth_openiduser', 'refresh_token', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Nonce.redirect_url'
        db.alter_column('oidc_auth_nonce', 'redirect_url', self.gf('django.db.models.fields.CharField')(max_length=100))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'oidc_auth.nonce': {
            'Meta': {'object_name': 'Nonce'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'redirect_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'state': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'oidc_auth.openidprovider': {
            'Meta': {'object_name': 'OpenIDProvider'},
            'authorization_endpoint': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'jwks_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'signing_alg': ('django.db.models.fields.CharField', [], {'default': "'HS256'", 'max_length': '5'}),
            'token_endpoint': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'userinfo_endpoint': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'oidc_auth.openiduser': {
            'Meta': {'object_name': 'OpenIDUser'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oidc_auth.OpenIDProvider']"}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'sub': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'oidc_account'", 'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['oidc_auth']
