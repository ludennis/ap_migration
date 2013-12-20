# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hcrecmd'
        db.create_table(u'HCRecmd', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'ResidenceID')),
            ('hcuserid', self.gf('django.db.models.fields.IntegerField')(db_column=u'HCUserID')),
            ('recmdhcuserid', self.gf('django.db.models.fields.IntegerField')(db_column=u'recmdHCUserID')),
            ('choice', self.gf('django.db.models.fields.IntegerField')()),
            ('evalcriterion1', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion1')),
            ('evalcriterion2', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion2')),
            ('evalcriterion3', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion3')),
            ('evalcriterion4', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion4')),
            ('evalcriterion5', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion5')),
            ('evalcriterion6', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion6')),
            ('evalcriterion7', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion7')),
            ('evalcriterion8', self.gf('django.db.models.fields.IntegerField')(db_column=u'evalCriterion8')),
            ('notes', self.gf('django.db.models.fields.TextField')(db_column=u'Notes', blank=True)),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
        ))
        db.send_create_signal(u'migrate', ['Hcrecmd'])

        # Adding model 'Hcrecmdcriteria'
        db.create_table(u'HCRecmdCriteria', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('min', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('max', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Hcrecmdcriteria'])

        # Adding model 'Accounttype'
        db.create_table(u'accountType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255L)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3L)),
            ('databasetable', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'databaseTable', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Accounttype'])

        # Adding model 'Announcementmember'
        db.create_table(u'announcementMember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('announcementrequestid', self.gf('django.db.models.fields.IntegerField')(db_column=u'announcementRequestID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('viewed', self.gf('django.db.models.fields.CharField')(max_length=3L)),
        ))
        db.send_create_signal(u'migrate', ['Announcementmember'])

        # Adding model 'Announcementrequest'
        db.create_table(u'announcementRequest', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('announcementtypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'announcementTypeID')),
            ('typevalue', self.gf('django.db.models.fields.TextField')(db_column=u'typeValue', blank=True)),
            ('datecreated', self.gf('django.db.models.fields.DateTimeField')(db_column=u'dateCreated')),
            ('announcement', self.gf('django.db.models.fields.TextField')()),
            ('purpose', self.gf('django.db.models.fields.TextField')()),
            ('date2announce', self.gf('django.db.models.fields.DateField')(db_column=u'date2Announce')),
            ('date2hide', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'date2Hide', blank=True)),
            ('announcementstatusid', self.gf('django.db.models.fields.IntegerField')(db_column=u'announcementStatusID')),
            ('showpaper', self.gf('django.db.models.fields.IntegerField')(db_column=u'showPaper')),
            ('showserver', self.gf('django.db.models.fields.IntegerField')(db_column=u'showServer')),
            ('showcommons', self.gf('django.db.models.fields.IntegerField')(db_column=u'showCommons')),
            ('tacomments', self.gf('django.db.models.fields.TextField')(db_column=u'TAComments', blank=True)),
            ('ta_userid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ta_userID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Announcementrequest'])

        # Adding model 'Announcementselection'
        db.create_table(u'announcementSelection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('announcementrequestid', self.gf('django.db.models.fields.IntegerField')(db_column=u'announcementRequestID')),
            ('foreignid', self.gf('django.db.models.fields.IntegerField')(db_column=u'foreignID')),
        ))
        db.send_create_signal(u'migrate', ['Announcementselection'])

        # Adding model 'Announcementstatus'
        db.create_table(u'announcementStatus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Announcementstatus'])

        # Adding model 'Announcementtype'
        db.create_table(u'announcementType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Announcementtype'])

        # Adding model 'Atrabsenttrainee'
        db.create_table(u'atrAbsentTrainee', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('atrrosterid', self.gf('django.db.models.fields.IntegerField')(db_column=u'atrRosterID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=17L)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('numdays', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDays', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Atrabsenttrainee'])

        # Adding model 'Atrroster'
        db.create_table(u'atrRoster', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('date', self.gf('django.db.models.fields.DateField')(unique=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Atrroster'])

        # Adding model 'Atrunreportedhouse'
        db.create_table(u'atrUnreportedHouse', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('atrrosterid', self.gf('django.db.models.fields.IntegerField')(db_column=u'atrRosterID')),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'residenceID')),
        ))
        db.send_create_signal(u'migrate', ['Atrunreportedhouse'])

        # Adding model 'Attendancesystem'
        db.create_table(u'attendancesystem', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100L)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3L)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('term1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('term2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('term3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('term4', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Attendancesystem'])

        # Adding model 'Attendancetables'
        db.create_table(u'attendancetables', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('tablename', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'tableName')),
        ))
        db.send_create_signal(u'migrate', ['Attendancetables'])

        # Adding model 'Avapprovalstatus'
        db.create_table(u'avApprovalStatus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('approvalstatus', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'approvalStatus')),
        ))
        db.send_create_signal(u'migrate', ['Avapprovalstatus'])

        # Adding model 'Avclass'
        db.create_table(u'avClass', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('classyear', self.gf('django.db.models.fields.IntegerField')(db_column=u'classYear')),
            ('dayofweek', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'dayOfWeek')),
            ('scheduleeventname', self.gf('django.db.models.fields.CharField')(max_length=45L, db_column=u'scheduleEventName')),
        ))
        db.send_create_signal(u'migrate', ['Avclass'])

        # Adding model 'Avreason'
        db.create_table(u'avReason', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Avreason'])

        # Adding model 'Avrequest'
        db.create_table(u'avRequest', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('avclassid', self.gf('django.db.models.fields.IntegerField')(db_column=u'avClassID')),
            ('classdate', self.gf('django.db.models.fields.DateField')(db_column=u'classDate')),
            ('avreasonid', self.gf('django.db.models.fields.IntegerField')(db_column=u'avReasonID')),
            ('datesubmitted', self.gf('django.db.models.fields.DateField')(db_column=u'dateSubmitted')),
            ('avapprovalstatusid', self.gf('django.db.models.fields.IntegerField')(db_column=u'avApprovalStatusID')),
            ('dateapproved', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dateApproved', blank=True)),
            ('avrequestcommentid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'avRequestCommentID', blank=True)),
            ('tacomments', self.gf('django.db.models.fields.TextField')(db_column=u'TAComments', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Avrequest'])

        # Adding model 'Avrequestcomment'
        db.create_table(u'avRequestComment', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('comments', self.gf('django.db.models.fields.TextField')(db_column=u'Comments', blank=True)),
            ('ta_userid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ta_userID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Avrequestcomment'])

        # Adding model 'Bostonapp'
        db.create_table(u'bostonApp', (
            ('application_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('submitted', self.gf('django.db.models.fields.IntegerField')()),
            ('trainee_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('sending_locality', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('age', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('citizenship', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('citizenship_other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('zip', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_chinese', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_spanish', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_korean', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bicycle', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('automobile', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('automobile_seats', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone_cell', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone_home', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('english_ability', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('major1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('degree1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('major2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('degree2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_saved', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_baptized', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('first_locality', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('first_locality_date', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('service_areas', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('previous_training', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('previous_training_graduation_date', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('marital_status', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouse_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouse_occupation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouse_age', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('marriage_date', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouse_attitude', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dependents', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_yourself', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_church', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_family_friends', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('other_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('statement', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Bostonapp'])

        # Adding model 'BrBooks'
        db.create_table(u'br_books', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30L)),
        ))
        db.send_create_signal(u'migrate', ['BrBooks'])

        # Adding model 'BrTraineeBook'
        db.create_table(u'br_trainee_book', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.BrBooks'])),
            ('trainee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'])),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Term'])),
        ))
        db.send_create_signal(u'migrate', ['BrTraineeBook'])

        # Adding model 'Bugs'
        db.create_table(u'bugs', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('assignedto_userid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'assignedTo_userID', blank=True)),
            ('datestarted', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'dateStarted')),
            ('projecteddate', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'projectedDate')),
            ('datecompleted', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'dateCompleted')),
            ('pageid', self.gf('django.db.models.fields.IntegerField')(db_column=u'pageID')),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(db_column=u'timeStamp')),
            ('bug', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('isdone', self.gf('django.db.models.fields.IntegerField')(db_column=u'isDone')),
            ('isvisible', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'isVisible')),
            ('priority', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('useragent', self.gf('django.db.models.fields.TextField')(db_column=u'userAgent', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Bugs'])

        # Adding model 'Bunk'
        db.create_table(u'bunk', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('roomid', self.gf('django.db.models.fields.IntegerField')(db_column=u'roomID')),
            ('bunkno', self.gf('django.db.models.fields.CharField')(max_length=8L, db_column=u'bunkNo', blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=6L, blank=True)),
            ('bunkid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'bunkID', blank=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fttause', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'fttaUse', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Bunk'])

        # Adding model 'Church'
        db.create_table(u'church', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Church'])

        # Adding model 'Classnotes'
        db.create_table(u'classNotes', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('rolleventid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Rollevent'], null=True, db_column=u'rollEventID', blank=True)),
            ('submissiondate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submissionDate')),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('finalized', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Classnotes'])

        # Adding model 'Conference'
        db.create_table(u'conference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('allergies', self.gf('django.db.models.fields.TextField')()),
            ('housing', self.gf('django.db.models.fields.IntegerField')()),
            ('paid', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Conference'])

        # Adding model 'Dailybibleverse'
        db.create_table(u'dailyBibleVerse', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('verseref', self.gf('django.db.models.fields.CharField')(max_length=30L, db_column=u'verseRef')),
            ('verse', self.gf('django.db.models.fields.TextField')()),
            ('dateadded', self.gf('django.db.models.fields.DateField')(db_column=u'dateAdded')),
            ('lastdisplayed', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'lastDisplayed', blank=True)),
            ('isdisplayed', self.gf('django.db.models.fields.IntegerField')(db_column=u'isDisplayed')),
        ))
        db.send_create_signal(u'migrate', ['Dailybibleverse'])

        # Adding model 'Dberror'
        db.create_table(u'dbError', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('file', self.gf('django.db.models.fields.CharField')(max_length=128L)),
            ('line', self.gf('django.db.models.fields.IntegerField')()),
            ('bugsid', self.gf('django.db.models.fields.IntegerField')(db_column=u'bugsID')),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('logpageid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'logPageID', blank=True)),
            ('error', self.gf('django.db.models.fields.TextField')()),
            ('query', self.gf('django.db.models.fields.TextField')()),
            ('stacktrace', self.gf('django.db.models.fields.TextField')(db_column=u'stackTrace')),
        ))
        db.send_create_signal(u'migrate', ['Dberror'])

        # Adding model 'Exams'
        db.create_table(u'exams', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('trainingclassesid', self.gf('django.db.models.fields.IntegerField')(db_column=u'trainingClassesID')),
            ('starttime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'startTime')),
            ('endtime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'endTime')),
            ('type', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('exam', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8L)),
        ))
        db.send_create_signal(u'migrate', ['Exams'])

        # Adding model 'Examstraineeaccess'
        db.create_table(u'examsTraineeAccess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('examid', self.gf('django.db.models.fields.IntegerField')(db_column=u'examID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
        ))
        db.send_create_signal(u'migrate', ['Examstraineeaccess'])

        # Adding model 'Examstraineeanswers'
        db.create_table(u'examsTraineeAnswers', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('lastupdated', self.gf('django.db.models.fields.DateTimeField')(db_column=u'lastUpdated')),
            ('examid', self.gf('django.db.models.fields.IntegerField')(db_column=u'examID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('answers', self.gf('django.db.models.fields.TextField')()),
            ('grade', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('finalized', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Examstraineeanswers'])

        # Adding model 'Examstraineeanswersgrades'
        db.create_table(u'examsTraineeAnswersGrades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('examstraineeanswersid', self.gf('django.db.models.fields.IntegerField')(db_column=u'examsTraineeAnswersID')),
            ('questionnumber', self.gf('django.db.models.fields.IntegerField')(db_column=u'questionNumber')),
            ('points', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=300L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Examstraineeanswersgrades'])

        # Adding model 'FrameRequests'
        db.create_table(u'frame_requests', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('residence_id', self.gf('django.db.models.fields.IntegerField')()),
            ('trainee_id', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('exists_already', self.gf('django.db.models.fields.IntegerField')()),
            ('fix', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('broken_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('frame_quote', self.gf('django.db.models.fields.TextField')()),
            ('completed', self.gf('django.db.models.fields.IntegerField')()),
            ('completed_date', self.gf('django.db.models.fields.DateField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['FrameRequests'])

        # Adding model 'Globalsettings'
        db.create_table(u'globalSettings', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32L, primary_key=True)),
            ('value', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Globalsettings'])

        # Adding model 'Gospelcitizenship'
        db.create_table(u'gospelCitizenship', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('citizenship', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Gospelcitizenship'])

        # Adding model 'Gospelsurvey'
        db.create_table(u'gospelSurvey', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('term', self.gf('django.db.models.fields.IntegerField')()),
            ('options', self.gf('django.db.models.fields.CharField')(max_length=40L)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=40L)),
        ))
        db.send_create_signal(u'migrate', ['Gospelsurvey'])

        # Adding model 'Gospeltripapplication'
        db.create_table(u'gospelTripApplication', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('pref1', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('preftext1', self.gf('django.db.models.fields.TextField')(db_column=u'prefText1', blank=True)),
            ('car1', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref2', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('preftext2', self.gf('django.db.models.fields.TextField')(db_column=u'prefText2', blank=True)),
            ('car2', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref3', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('preftext3', self.gf('django.db.models.fields.TextField')(db_column=u'prefText3', blank=True)),
            ('car3', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref4', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('preftext4', self.gf('django.db.models.fields.TextField')(db_column=u'prefText4', blank=True)),
            ('car4', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref5', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('preftext5', self.gf('django.db.models.fields.TextField')(db_column=u'prefText5', blank=True)),
            ('car5', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref6', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('preftext6', self.gf('django.db.models.fields.TextField')(db_column=u'prefText6', blank=True)),
            ('car6', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('lang1', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prof1', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('langtext1', self.gf('django.db.models.fields.TextField')(db_column=u'langText1', blank=True)),
            ('lang2', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prof2', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('langtext2', self.gf('django.db.models.fields.TextField')(db_column=u'langText2', blank=True)),
            ('lang3', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prof3', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('langtext3', self.gf('django.db.models.fields.TextField')(db_column=u'langText3', blank=True)),
            ('lang4', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prof4', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('langtext4', self.gf('django.db.models.fields.TextField')(db_column=u'langText4', blank=True)),
            ('lang5', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prof5', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('langtext5', self.gf('django.db.models.fields.TextField')(db_column=u'langText5', blank=True)),
            ('lang6', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prof6', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('langtext6', self.gf('django.db.models.fields.TextField')(db_column=u'langText6', blank=True)),
            ('show', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripapplication'])

        # Adding model 'Gospeltriparrangement'
        db.create_table(u'gospelTripArrangement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('gospeltriprunid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Gospeltriprun'], db_column=u'gospelTripRunID')),
        ))
        db.send_create_signal(u'migrate', ['Gospeltriparrangement'])

        # Adding model 'Gospeltripassignment'
        db.create_table(u'gospelTripAssignment', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('deposit', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('balance', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('balancepaid', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'balancePaid', blank=True)),
            ('gospeltripdestinationid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'gospelTripDestinationID', blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('datepaid', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'datePaid', blank=True)),
            ('paymentmethod', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'paymentMethod', blank=True)),
            ('generalcomment', self.gf('django.db.models.fields.TextField')(db_column=u'generalComment', blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=7L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripassignment'])

        # Adding model 'Gospeltripdestination'
        db.create_table(u'gospelTripDestination', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('gospeltypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'gospelTypeID')),
            ('secondyear', self.gf('django.db.models.fields.IntegerField')(db_column=u'secondYear')),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripdestination'])

        # Adding model 'Gospeltripdriver'
        db.create_table(u'gospelTripDriver', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripdriver'])

        # Adding model 'Gospeltripflight'
        db.create_table(u'gospelTripFlight', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('outflightnumber', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'outFlightNumber', blank=True)),
            ('outairline', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'outAirline', blank=True)),
            ('outdeptairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'outDeptAirport', blank=True)),
            ('outdeptdatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'outDeptDateTime', blank=True)),
            ('outarrivalairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'outArrivalAirport', blank=True)),
            ('outarrivaldatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'outArrivalDateTime', blank=True)),
            ('retflightnumber', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'retFlightNumber', blank=True)),
            ('retairline', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'retAirline', blank=True)),
            ('retdeptairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'retDeptAirport', blank=True)),
            ('retdeptdatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'retDeptDateTime', blank=True)),
            ('retarrivalairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'retArrivalAirport', blank=True)),
            ('retarrivaldatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'retArrivalDateTime', blank=True)),
            ('flightcomment', self.gf('django.db.models.fields.TextField')(db_column=u'flightComment', blank=True)),
            ('interoutflightnumber', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interOutFlightNumber', blank=True)),
            ('interoutairline', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interOutAirline', blank=True)),
            ('interoutdeptairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interOutDeptAirport', blank=True)),
            ('interoutdeptdatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'interOutDeptDateTime', blank=True)),
            ('interoutarrivalairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interOutArrivalAirport', blank=True)),
            ('interoutarrivaldatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'interOutArrivalDateTime', blank=True)),
            ('interretflightnumber', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interRetFlightNumber', blank=True)),
            ('interretairline', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interRetAirline', blank=True)),
            ('interretdeptairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interRetDeptAirport', blank=True)),
            ('interretdeptdatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'interRetDeptDateTime', blank=True)),
            ('interretarrivalairport', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'interRetArrivalAirport', blank=True)),
            ('interretarrivaldatetime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'interRetArrivalDateTime', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripflight'])

        # Adding model 'Gospeltripinformation'
        db.create_table(u'gospelTripInformation', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('mname', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('gospelcitizenshipid', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'gospelCitizenshipID')),
            ('vehicle', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('vehicleinsurance', self.gf('django.db.models.fields.CharField')(max_length=200L, db_column=u'vehicleInsurance', blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('allergy', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('costcovered', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'costCovered')),
            ('flightcovered', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'flightCovered')),
            ('costavailable', self.gf('django.db.models.fields.CharField')(max_length=200L, db_column=u'costAvailable', blank=True)),
            ('vehicleavailable', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'vehicleAvailable')),
            ('departingairport', self.gf('django.db.models.fields.CharField')(max_length=200L, db_column=u'departingAirport', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripinformation'])

        # Adding model 'Gospeltriplanguage'
        db.create_table(u'gospelTripLanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltriplanguage'])

        # Adding model 'Gospeltripoverseer'
        db.create_table(u'gospelTripOverseer', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=200L, db_column=u'firstName', blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=200L, db_column=u'lastName', blank=True)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('pref1', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('preftext1', self.gf('django.db.models.fields.TextField')(db_column=u'prefText1', blank=True)),
            ('car1', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref2', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('preftext2', self.gf('django.db.models.fields.TextField')(db_column=u'prefText2', blank=True)),
            ('car2', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref3', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('preftext3', self.gf('django.db.models.fields.TextField')(db_column=u'prefText3', blank=True)),
            ('car3', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref4', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('preftext4', self.gf('django.db.models.fields.TextField')(db_column=u'prefText4', blank=True)),
            ('car4', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref5', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('preftext5', self.gf('django.db.models.fields.TextField')(db_column=u'prefText5', blank=True)),
            ('car5', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('pref6', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('preftext6', self.gf('django.db.models.fields.TextField')(db_column=u'prefText6', blank=True)),
            ('car6', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('lang1', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('prof1', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('langtext1', self.gf('django.db.models.fields.TextField')(db_column=u'langText1', blank=True)),
            ('lang2', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('prof2', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('langtext2', self.gf('django.db.models.fields.TextField')(db_column=u'langText2', blank=True)),
            ('lang3', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('prof3', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('langtext3', self.gf('django.db.models.fields.TextField')(db_column=u'langText3', blank=True)),
            ('lang4', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('prof4', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('langtext4', self.gf('django.db.models.fields.TextField')(db_column=u'langText4', blank=True)),
            ('lang5', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('prof5', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('langtext5', self.gf('django.db.models.fields.TextField')(db_column=u'langText5', blank=True)),
            ('lang6', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('prof6', self.gf('django.db.models.fields.CharField')(max_length=200L, blank=True)),
            ('langtext6', self.gf('django.db.models.fields.TextField')(db_column=u'langText6', blank=True)),
            ('contact', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripoverseer'])

        # Adding model 'Gospeltrippassport'
        db.create_table(u'gospelTripPassport', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('mname', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('citizenship', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('gospelcitizenshipid', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'gospelCitizenshipID')),
            ('gospelcitizenshipother', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'gospelCitizenshipOther', blank=True)),
            ('expirationdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'expirationDate', blank=True)),
            ('passportnumber', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'passportNumber', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltrippassport'])

        # Adding model 'Gospeltrippayment'
        db.create_table(u'gospelTripPayment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payment', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltrippayment'])

        # Adding model 'Gospeltripproficiency'
        db.create_table(u'gospelTripProficiency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proficiency', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripproficiency'])

        # Adding model 'Gospeltriprun'
        db.create_table(u'gospelTripRun', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200L)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('startloc', self.gf('django.db.models.fields.CharField')(max_length=200L, db_column=u'startLoc', blank=True)),
            ('endloc', self.gf('django.db.models.fields.CharField')(max_length=200L, db_column=u'endLoc', blank=True)),
            ('gospeltripvehicleid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Gospeltripvehicle'], null=True, db_column=u'gospelTripVehicleID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltriprun'])

        # Adding model 'Gospeltriprundriver'
        db.create_table(u'gospelTripRunDriver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gospeltriprunid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Gospeltriprun'], db_column=u'gospelTripRunID')),
            ('gospeltripdriverid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Gospeltripdriver'], db_column=u'gospelTripDriverID')),
        ))
        db.send_create_signal(u'migrate', ['Gospeltriprundriver'])

        # Adding model 'Gospeltripselection'
        db.create_table(u'gospelTripSelection', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('gospeltypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'gospelTypeID')),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripselection'])

        # Adding model 'Gospeltripvehicle'
        db.create_table(u'gospelTripVehicle', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('vehiclename', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'vehicleName')),
            ('numpassenger', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numPassenger', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltripvehicle'])

        # Adding model 'Gospeltype'
        db.create_table(u'gospelType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Gospeltype'])

        # Adding model 'Gp'
        db.create_table(u'gp', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('active', self.gf('django.db.models.fields.IntegerField')(db_column=u'Active')),
            ('gpid', self.gf('django.db.models.fields.IntegerField')(db_column=u'gpID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('termname', self.gf('django.db.models.fields.CharField')(max_length=45L, db_column=u'termName')),
        ))
        db.send_create_signal(u'migrate', ['Gp'])

        # Adding model 'Gpstats'
        db.create_table(u'gpStats', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('gpid', self.gf('django.db.models.fields.IntegerField')(db_column=u'gpID')),
            ('week', self.gf('django.db.models.fields.IntegerField')()),
            ('gptypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'gpTypeID')),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('teamid', self.gf('django.db.models.fields.IntegerField')(db_column=u'teamID')),
            ('termname', self.gf('django.db.models.fields.CharField')(max_length=45L, db_column=u'termName')),
        ))
        db.send_create_signal(u'migrate', ['Gpstats'])

        # Adding model 'Gpteam'
        db.create_table(u'gpTeam', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('gpid', self.gf('django.db.models.fields.IntegerField')(db_column=u'gpID')),
            ('teamid', self.gf('django.db.models.fields.IntegerField')(db_column=u'teamID')),
        ))
        db.send_create_signal(u'migrate', ['Gpteam'])

        # Adding model 'Gptype'
        db.create_table(u'gpType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('statname', self.gf('django.db.models.fields.CharField')(max_length=26L, db_column=u'statName')),
        ))
        db.send_create_signal(u'migrate', ['Gptype'])

        # Adding model 'GradActivity'
        db.create_table(u'grad_activity', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['GradActivity'])

        # Adding model 'GradAdmin'
        db.create_table(u'grad_admin', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('gradactivityid', self.gf('django.db.models.fields.IntegerField')(db_column=u'gradActivityID')),
            ('showactivity', self.gf('django.db.models.fields.IntegerField')(db_column=u'showActivity')),
            ('duedate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dueDate', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['GradAdmin'])

        # Adding model 'GradConsiderations'
        db.create_table(u'grad_considerations', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('attend', self.gf('django.db.models.fields.CharField')(max_length=4L, blank=True)),
            ('fellowship', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('finance', self.gf('django.db.models.fields.CharField')(max_length=4L, blank=True)),
            ('plans', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['GradConsiderations'])

        # Adding model 'GradInvites'
        db.create_table(u'grad_invites', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('num_invites', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_dvd', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['GradInvites'])

        # Adding model 'GradRemembrance'
        db.create_table(u'grad_remembrance', (
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'traineeID')),
            ('remembrance1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('remembrance2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('reference', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('localityid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'localityID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['GradRemembrance'])

        # Adding model 'GradSpeaking'
        db.create_table(u'grad_speaking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('speaking', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['GradSpeaking'])

        # Adding model 'GradStats'
        db.create_table(u'grad_stats', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('num_invites', self.gf('django.db.models.fields.IntegerField')()),
            ('burden1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('burden2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('burden3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pref1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pref2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pref3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('q1', self.gf('django.db.models.fields.IntegerField')()),
            ('q2', self.gf('django.db.models.fields.TextField')()),
            ('q3', self.gf('django.db.models.fields.TextField')()),
            ('q4', self.gf('django.db.models.fields.IntegerField')()),
            ('plans', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['GradStats'])

        # Adding model 'GradSurvey'
        db.create_table(u'grad_survey', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('outlinesections', self.gf('django.db.models.fields.IntegerField')(db_column=u'outlineSections')),
            ('outline', self.gf('django.db.models.fields.TextField')()),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
        ))
        db.send_create_signal(u'migrate', ['GradSurvey'])

        # Adding model 'GradTestimony'
        db.create_table(u'grad_testimony', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'traineeID', blank=True)),
            ('termid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'termID', blank=True)),
            ('testimony', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fellowship', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('question3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('question4', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('testimony_speak', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fellowship_speak', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mod_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'migrate', ['GradTestimony'])

        # Adding model 'Greekparsing'
        db.create_table(u'greekParsing', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Greekparsing'])

        # Adding model 'Greekuserstats'
        db.create_table(u'greekUserStats', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('greekvocabid', self.gf('django.db.models.fields.IntegerField')(db_column=u'greekVocabID')),
            ('numtimes', self.gf('django.db.models.fields.IntegerField')(db_column=u'numTimes')),
            ('correct', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Greekuserstats'])

        # Adding model 'Greekvocab'
        db.create_table(u'greekVocab', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('greek', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('english', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('chapter', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('parsingid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'parsingID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Greekvocab'])

        # Adding model 'Gtcasurvey'
        db.create_table(u'gtcaSurvey', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('term', self.gf('django.db.models.fields.IntegerField')()),
            ('college', self.gf('django.db.models.fields.TextField')()),
            ('major', self.gf('django.db.models.fields.TextField')()),
            ('locality', self.gf('django.db.models.fields.TextField')()),
            ('charlottesville', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('fortcollins', self.gf('django.db.models.fields.CharField')(max_length=5L, db_column=u'fortCollins')),
            ('madison', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('philadelphia', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('montreal', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('capacity', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('released', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('fellowship', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('joinmonth', self.gf('django.db.models.fields.IntegerField')(db_column=u'joinMonth')),
            ('joinyear', self.gf('django.db.models.fields.IntegerField')(db_column=u'joinYear')),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Gtcasurvey'])

        # Adding model 'Hcsurvey'
        db.create_table(u'hcSurvey', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'ResidenceID')),
            ('hcuserid', self.gf('django.db.models.fields.IntegerField')(db_column=u'HCUserID')),
            ('periodid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'periodID', blank=True)),
            ('atmosphere', self.gf('django.db.models.fields.TextField')()),
            ('situations', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Hcsurvey'])

        # Adding model 'Hcsurveytraineenotes'
        db.create_table(u'hcSurveyTraineeNotes', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('hcsurveyid', self.gf('django.db.models.fields.IntegerField')(db_column=u'hcSurveyID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Hcsurveytraineenotes'])

        # Adding model 'Hcrecmdqs'
        db.create_table(u'hcrecmdqs', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'ResidenceID')),
            ('hcuserid', self.gf('django.db.models.fields.IntegerField')(db_column=u'HCUserID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('atmosphere', self.gf('django.db.models.fields.TextField')()),
            ('situations', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Hcrecmdqs'])

        # Adding model 'Houseinspectionfaq'
        db.create_table(u'houseInspectionFAQ', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('useful', self.gf('django.db.models.fields.IntegerField')()),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=14L)),
            ('askerid', self.gf('django.db.models.fields.IntegerField')(db_column=u'askerID')),
        ))
        db.send_create_signal(u'migrate', ['Houseinspectionfaq'])

        # Adding model 'Importsql'
        db.create_table(u'importSQL', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('transactionid', self.gf('django.db.models.fields.IntegerField')(db_column=u'transactionID')),
            ('sqlstatement', self.gf('django.db.models.fields.TextField')(db_column=u'sqlStatement')),
            ('undostatement', self.gf('django.db.models.fields.TextField')(db_column=u'undoStatement', blank=True)),
            ('iscompleted', self.gf('django.db.models.fields.IntegerField')(db_column=u'isCompleted')),
        ))
        db.send_create_signal(u'migrate', ['Importsql'])

        # Adding model 'Importsqlauthor'
        db.create_table(u'importSQLAuthor', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('transactionid', self.gf('django.db.models.fields.IntegerField')(db_column=u'transactionID')),
            ('timebegin', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'timeBegin', blank=True)),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('isfinished', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'isFinished', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Importsqlauthor'])

        # Adding model 'ImportTrainee'
        db.create_table(u'import_trainee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.TextField')(db_column=u'firstName', blank=True)),
            ('nickname', self.gf('django.db.models.fields.TextField')(db_column=u'nickName', blank=True)),
            ('lastname', self.gf('django.db.models.fields.TextField')(db_column=u'lastName', blank=True)),
            ('middleinitial', self.gf('django.db.models.fields.TextField')(db_column=u'middleInitial', blank=True)),
            ('maidenname', self.gf('django.db.models.fields.TextField')(db_column=u'maidenName', blank=True)),
            ('birthdate', self.gf('django.db.models.fields.TextField')(db_column=u'birthDate', blank=True)),
            ('gender', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('zip', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('maritalstatus', self.gf('django.db.models.fields.TextField')(db_column=u'maritalStatus', blank=True)),
            ('phonenumber', self.gf('django.db.models.fields.TextField')(db_column=u'phoneNumber', blank=True)),
            ('cellnumber', self.gf('django.db.models.fields.TextField')(db_column=u'cellNumber', blank=True)),
            ('email', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sendinglocality', self.gf('django.db.models.fields.TextField')(db_column=u'sendingLocality', blank=True)),
            ('datebegin', self.gf('django.db.models.fields.TextField')(db_column=u'dateBegin', blank=True)),
            ('termscompleted', self.gf('django.db.models.fields.TextField')(db_column=u'termsCompleted', blank=True)),
            ('couple', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('emergencycontact', self.gf('django.db.models.fields.TextField')(db_column=u'emergencyContact', blank=True)),
            ('emergencyaddress', self.gf('django.db.models.fields.TextField')(db_column=u'emergencyAddress', blank=True)),
            ('emergencyphone', self.gf('django.db.models.fields.TextField')(db_column=u'emergencyPhone', blank=True)),
            ('emergencyphone2', self.gf('django.db.models.fields.TextField')(db_column=u'emergencyPhone2', blank=True)),
            ('readot', self.gf('django.db.models.fields.TextField')(db_column=u'readOT', blank=True)),
            ('readnt', self.gf('django.db.models.fields.TextField')(db_column=u'readNT', blank=True)),
            ('ta', self.gf('django.db.models.fields.TextField')(db_column=u'TA', blank=True)),
            ('mentor', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('major', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('degree', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gospelpref1', self.gf('django.db.models.fields.TextField')(db_column=u'gospelPref1', blank=True)),
            ('gospelpref2', self.gf('django.db.models.fields.TextField')(db_column=u'gospelPref2', blank=True)),
            ('vehicleinfo', self.gf('django.db.models.fields.TextField')(db_column=u'vehicleInfo', blank=True)),
            ('vehiclelicense', self.gf('django.db.models.fields.TextField')(db_column=u'vehicleLicense', blank=True)),
            ('vehiclecolor', self.gf('django.db.models.fields.TextField')(db_column=u'vehicleColor', blank=True)),
            ('vehiclecapacity', self.gf('django.db.models.fields.TextField')(db_column=u'vehicleCapacity', blank=True)),
            ('residenceid', self.gf('django.db.models.fields.TextField')(db_column=u'residenceID', blank=True)),
            ('officeid', self.gf('django.db.models.fields.TextField')(db_column=u'officeID', blank=True)),
            ('stpt', self.gf('django.db.models.fields.TextField')(db_column=u'STPT', blank=True)),
            ('stft', self.gf('django.db.models.fields.TextField')(db_column=u'STFT', blank=True)),
            ('teamid', self.gf('django.db.models.fields.TextField')(db_column=u'teamID', blank=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'traineeID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['ImportTrainee'])

        # Adding model 'Inspectionscore'
        db.create_table(u'inspectionScore', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('inspectoruserid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'inspectorUserID', blank=True)),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'residenceID')),
            ('score', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ricuserid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'RICUserID', blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('uninspectable', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Inspectionscore'])

        # Adding model 'Interimcalendar'
        db.create_table(u'interimCalendar', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('startdate', self.gf('django.db.models.fields.DateField')(db_column=u'startDate')),
            ('enddate', self.gf('django.db.models.fields.DateField')(db_column=u'endDate')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Interimcalendar'])

        # Adding model 'Interimexit'
        db.create_table(u'interimExit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('interimintentionid', self.gf('django.db.models.fields.IntegerField')(db_column=u'interimIntentionID')),
            ('unsure', self.gf('django.db.models.fields.CharField')(max_length=3L)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Interimexit'])

        # Adding model 'Interimintention'
        db.create_table(u'interimIntention', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('placeholder', self.gf('django.db.models.fields.TextField')(db_column=u'placeHolder', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Interimintention'])

        # Adding model 'Leaveslip'
        db.create_table(u'leaveSlip', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], db_column=u'userID')),
            ('leaveslipcategoryid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Leaveslipcategory'], db_column=u'leaveSlipCategoryID')),
            ('submissiondatetime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submissionDateTime')),
            ('remarks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('requiresfellowship', self.gf('django.db.models.fields.IntegerField')(db_column=u'requiresFellowship')),
            ('assignedtaid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'assignedTAID', blank=True)),
            ('informeduserid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'informedUserID', blank=True)),
            ('taremarks', self.gf('django.db.models.fields.TextField')(db_column=u'TARemarks', blank=True)),
            ('taprivateremarks', self.gf('django.db.models.fields.TextField')(db_column=u'TAPrivateRemarks', blank=True)),
            ('haspaperleaveslip', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'hasPaperLeaveSlip', blank=True)),
            ('svscheduleinstanceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svscheduleinstance'], null=True, db_column=u'svScheduleInstanceID', blank=True)),
            ('svserviceid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svServiceID', blank=True)),
            ('sistertaapproval', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'sisterTAApproval', blank=True)),
            ('didnotinform', self.gf('django.db.models.fields.IntegerField')(db_column=u'didNotInform')),
            ('texted', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Leaveslip'])

        # Adding model 'Leaveslipapproval'
        db.create_table(u'leaveSlipApproval', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('leaveslipid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Leaveslip'], unique=True, db_column=u'leaveSlipID')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], db_column=u'userID')),
            ('approvaldatetime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'approvalDateTime')),
            ('approvalstatus', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'approvalStatus')),
            ('remarks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('affectsperfectattendance', self.gf('django.db.models.fields.IntegerField')(db_column=u'affectsPerfectAttendance')),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipapproval'])

        # Adding model 'Leaveslipcategory'
        db.create_table(u'leaveSlipCategory', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('leavesliptypeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Leavesliptype'], db_column=u'leaveSlipTypeID')),
            ('affectsperfectattendance', self.gf('django.db.models.fields.IntegerField')(db_column=u'affectsPerfectAttendance')),
            ('special', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipcategory'])

        # Adding model 'Leaveslipevent'
        db.create_table(u'leaveSlipEvent', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('leaveslipid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Leaveslip'], db_column=u'leaveSlipID')),
            ('scheduleeventid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Scheduleevent'], db_column=u'scheduleEventID')),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipevent'])

        # Adding model 'Leaveslipmealout'
        db.create_table(u'leaveSlipMealOut', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('leaveslipid', self.gf('django.db.models.fields.IntegerField')(db_column=u'leaveSlipID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64L, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipmealout'])

        # Adding model 'Leaveslipmember'
        db.create_table(u'leaveSlipMember', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('leaveslipid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Leaveslip'], db_column=u'leaveSlipID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipmember'])

        # Adding model 'Leaveslipnightout'
        db.create_table(u'leaveSlipNightOut', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('leaveslipid', self.gf('django.db.models.fields.IntegerField')(db_column=u'leaveSlipID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64L, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=14L, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('hcname', self.gf('django.db.models.fields.CharField')(max_length=30L, db_column=u'HCname', blank=True)),
            ('verifyhc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'verifyHC', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipnightout'])

        # Adding model 'Leaveslipstatus'
        db.create_table(u'leaveSlipStatus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2L, db_column=u'statusCode')),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipstatus'])

        # Adding model 'Leaveslipta'
        db.create_table(u'leaveSlipTA', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('leaveslipid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'leaveSlipID', blank=True)),
            ('trainingassistantid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'trainingAssistantID', blank=True)),
            ('date_assigned', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipta'])

        # Adding model 'Leavesliptype'
        db.create_table(u'leaveSlipType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
        ))
        db.send_create_signal(u'migrate', ['Leavesliptype'])

        # Adding model 'Leaveslipgroupview'
        db.create_table(u'leaveslipgroupview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheduleeventid', self.gf('django.db.models.fields.IntegerField')(db_column=u'scheduleEventID')),
            ('leaveslipid', self.gf('django.db.models.fields.IntegerField')(db_column=u'leaveSlipID')),
            ('leaveslipcategoryid', self.gf('django.db.models.fields.IntegerField')(db_column=u'leaveSlipCategoryID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'migrate', ['Leaveslipgroupview'])

        # Adding model 'LeaveslipinfoGroup'
        db.create_table(u'leaveslipinfo_group', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('leaveslipid', self.gf('django.db.models.fields.IntegerField')(db_column=u'leaveSlipID')),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('starttime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'startTime')),
            ('endtime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'endTime')),
        ))
        db.send_create_signal(u'migrate', ['LeaveslipinfoGroup'])

        # Adding model 'Leaveslippersonalview'
        db.create_table(u'leaveslippersonalview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheduleeventid', self.gf('django.db.models.fields.IntegerField')(db_column=u'scheduleEventID')),
            ('leaveslipid', self.gf('django.db.models.fields.IntegerField')(db_column=u'leaveSlipID')),
            ('leaveslipcategoryid', self.gf('django.db.models.fields.IntegerField')(db_column=u'leaveSlipCategoryID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'migrate', ['Leaveslippersonalview'])

        # Adding model 'LinensRequests'
        db.create_table(u'linens_requests', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('residence_id', self.gf('django.db.models.fields.IntegerField')()),
            ('trainee_id', self.gf('django.db.models.fields.IntegerField')()),
            ('item_id', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('completed', self.gf('django.db.models.fields.IntegerField')()),
            ('completed_date', self.gf('django.db.models.fields.DateField')()),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['LinensRequests'])

        # Adding model 'LinensTypes'
        db.create_table(u'linens_types', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['LinensTypes'])

        # Adding model 'Locality'
        db.create_table(u'locality', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('city', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255L, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mrtype', self.gf('django.db.models.fields.IntegerField')(db_column=u'MRType')),
        ))
        db.send_create_signal(u'migrate', ['Locality'])

        # Adding model 'Logbrowser'
        db.create_table(u'logBrowser', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Logbrowser'])

        # Adding model 'Logclasslogin'
        db.create_table(u'logClassLogin', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('ipaddress', self.gf('django.db.models.fields.CharField')(max_length=15L, db_column=u'ipAddress')),
            ('session', self.gf('django.db.models.fields.CharField')(max_length=32L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Logclasslogin'])

        # Adding model 'Loglogin'
        db.create_table(u'logLogin', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=32L)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=7L)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('ipaddr', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ipAddr', blank=True)),
            ('session', self.gf('django.db.models.fields.CharField')(max_length=32L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Loglogin'])

        # Adding model 'Lognightlytasks'
        db.create_table(u'logNightlyTasks', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32L)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('messages', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Lognightlytasks'])

        # Adding model 'Logpage'
        db.create_table(u'logPage', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'userID', blank=True)),
            ('pageid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'pageID', blank=True)),
            ('pageurl', self.gf('django.db.models.fields.TextField')(db_column=u'pageUrl', blank=True)),
            ('browserid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'browserID', blank=True)),
            ('postparam', self.gf('django.db.models.fields.TextField')(db_column=u'postParam', blank=True)),
            ('getparam', self.gf('django.db.models.fields.TextField')(db_column=u'getParam', blank=True)),
            ('starttime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'startTime')),
            ('endtime', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'endTime', blank=True)),
            ('loadtime', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'loadTime', blank=True)),
            ('session', self.gf('django.db.models.fields.CharField')(max_length=32L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Logpage'])

        # Adding model 'Lookup'
        db.create_table(u'lookup', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('value', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Lookup'])

        # Adding model 'Lsbook'
        db.create_table(u'lsBook', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32L, blank=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=8L, blank=True)),
            ('nummessages', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numMessages', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Lsbook'])

        # Adding model 'Lsoffense'
        db.create_table(u'lsOffense', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('lsoffensereasonid', self.gf('django.db.models.fields.IntegerField')(db_column=u'lsOffenseReasonID')),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('creationdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'creationDate')),
            ('lastupdatedate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'lastUpdateDate')),
            ('iscurrentlymondayoffense', self.gf('django.db.models.fields.IntegerField')(db_column=u'isCurrentlyMondayOffense')),
            ('numlsowed', self.gf('django.db.models.fields.IntegerField')(db_column=u'numLSOwed')),
            ('numlsreceived', self.gf('django.db.models.fields.IntegerField')(db_column=u'numLSReceived')),
            ('signedin', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'signedIn', blank=True)),
            ('manualhandling', self.gf('django.db.models.fields.IntegerField')(db_column=u'manualHandling')),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('tacomments', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'taComments', blank=True)),
            ('numlsunapplied', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numLSUnapplied', blank=True)),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
        ))
        db.send_create_signal(u'migrate', ['Lsoffense'])

        # Adding model 'Lsoffensereason'
        db.create_table(u'lsOffenseReason', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('offensereason', self.gf('django.db.models.fields.CharField')(max_length=30L, db_column=u'offenseReason')),
            ('ismondayoffense', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'isMondayOffense', blank=True)),
            ('numls', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numLS', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Lsoffensereason'])

        # Adding model 'Lssubmission'
        db.create_table(u'lsSubmission', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('lsoffenseid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'lsOffenseID', blank=True)),
            ('lsbookid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'lsBookID', blank=True)),
            ('messagenumber', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'messageNumber', blank=True)),
            ('submissiondate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submissionDate')),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('finalized', self.gf('django.db.models.fields.IntegerField')()),
            ('approved', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Lssubmission'])

        # Adding model 'MaintenanceRequests'
        db.create_table(u'maintenance_requests', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('type_id', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('residence_id', self.gf('django.db.models.fields.IntegerField')()),
            ('room_id', self.gf('django.db.models.fields.IntegerField')()),
            ('other_room', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('trainee_id', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('completed', self.gf('django.db.models.fields.IntegerField')()),
            ('completed_date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['MaintenanceRequests'])

        # Adding model 'MaintenanceTypes'
        db.create_table(u'maintenance_types', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['MaintenanceTypes'])

        # Adding model 'Mealseatlocation'
        db.create_table(u'mealSeatLocation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=9L)),
        ))
        db.send_create_signal(u'migrate', ['Mealseatlocation'])

        # Adding model 'Mealseating'
        db.create_table(u'mealSeating', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('numberoccupied', self.gf('django.db.models.fields.IntegerField')(db_column=u'numberOccupied')),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
            ('maxcapacity', self.gf('django.db.models.fields.IntegerField')(db_column=u'maxCapacity')),
            ('mealseatlocationid', self.gf('django.db.models.fields.IntegerField')(db_column=u'mealSeatLocationID')),
        ))
        db.send_create_signal(u'migrate', ['Mealseating'])

        # Adding model 'Newapplications'
        db.create_table(u'newApplications', (
            ('applicationid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'applicationID')),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('mname', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('lname', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gender', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('locality', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('zip', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone_home', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone_cell', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone_international_home', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone_international_cell', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('birth_date', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('citizenship', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('automobile', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('automobile_seats', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_chinese', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_spanish', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_korean', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('otherlang', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('major', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('degree', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('major2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('degree2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('occupation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('full_time_date', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('datesaved', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('datebaptized', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('churchdate', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('firstcontact', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('serviceareas', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('previoustraining', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('read_ot', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('read_nt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('maritalstatus', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spousename', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dateofmarriage', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouseoccupation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouseage', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouseattitude', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dependent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_yourself', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_church', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_family', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('support_other_value', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pertinantinformation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med2list', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med3list', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_4', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_5', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_6', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_7', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4_8', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med4list', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med5', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med6', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med7', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med8', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_4', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_5', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_6', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_7', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_8', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_9', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med9_10', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med10', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med11', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med12', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med13', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med14', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med15', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med16', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tobacco', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med17_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('alcohol', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med17_2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('drugs', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med17_3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('exam', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med18', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('xray', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med19', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med20', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med21', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med22', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med23_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med23_2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med24', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med25', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('td_test', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hepatitisa1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hepatitisa2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hepatitisb1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hepatitisb2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hepatitisb3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tbdate', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tbresult', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('xraydate', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cxrayresult', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mmr1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mmr2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('immunizations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('height', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('weight', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med28', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med28_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med30', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('emergencyname', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('emergencyaddress', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('emergencytelephone', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('emergencyemail', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('insurance', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('health_concerns', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('testimony', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('poor_english', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gospelpref1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gospelpref2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('aka', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('audio_video', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('auto_mechanics', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('automobile_color', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('automobile_license', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('automobile_model', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bachelors', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('carpentry', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('citizen', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comp_database', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comp_hardware', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comp_networking', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comp_programming', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('electrical', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('emergencytelephone2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('facility_maint', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('floor_covering', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gardening', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('graphic_design', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('landscaping', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_or_char', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('locality_country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('locality_state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('locality_other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('locality_other_country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('maidenname', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('medical_training', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('photography', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('picture_framing', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('plumbing', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('prof_writing', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('security_safety', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sewing', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('skills_other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('terms', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('web_programming', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('med6a', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_recommendation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_participation', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('elder_knowledge', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('elder_work_together', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('elder_work_ethic', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('elder_in_relationship', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('elder_relationship_explain', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_understand_relationship_restriction', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('elder_understand_possible_dismissal', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('elder_abide_relationship_restriction', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('elder_understand_english', self.gf('django.db.models.fields.CharField')(max_length=3L, blank=True)),
            ('elder_recommend', self.gf('django.db.models.fields.CharField')(max_length=16L, blank=True)),
            ('elder_shepherd', self.gf('django.db.models.fields.CharField')(max_length=64L, blank=True)),
            ('elder_shepherd_cell', self.gf('django.db.models.fields.CharField')(max_length=32L, blank=True)),
            ('elder_shepherd_email', self.gf('django.db.models.fields.CharField')(max_length=64L, blank=True)),
            ('elder_elderfname', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_elderlname', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_elderemail', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_eldercell', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_paper_recommendation', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('deleted', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('raisedinchurch', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('attend_two_years', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('attend_explain', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college_grad_date', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('skype', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college_country', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('college2_country', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('previoustraining2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('twitter', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_mandarin', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lang_cantonese', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouse_attending', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spouse_plans', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('previoustrainingdate', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('medapproval', self.gf('django.db.models.fields.CharField')(max_length=18L, blank=True)),
            ('approval', self.gf('django.db.models.fields.CharField')(max_length=13L, blank=True)),
            ('consecration', self.gf('django.db.models.fields.CharField')(max_length=15L, blank=True)),
            ('med_comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('internationalforms', self.gf('django.db.models.fields.CharField')(max_length=84L, db_column=u'internationalForms', blank=True)),
            ('overseer_comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('international_comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elder_erec_complete', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'elder_eRec_complete', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Newapplications'])

        # Adding model 'Newapplicationsstatus'
        db.create_table(u'newApplicationsStatus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('newapplicationsid', self.gf('django.db.models.fields.IntegerField')(db_column=u'newApplicationsID')),
            ('approveddennis', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'approvedDennis')),
            ('approvedandrew', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'approvedAndrew')),
            ('approvedmedical', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'approvedMedical')),
            ('provisionalmedical', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'provisionalMedical')),
            ('approvedoverall', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'approvedOverall')),
            ('provisionalacceptance', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'provisionalAcceptance')),
            ('sentacknowledgement', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentAcknowledgement')),
            ('sentacceptance', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentAcceptance')),
            ('timestampsentacknowledgement', self.gf('django.db.models.fields.DateTimeField')(db_column=u'timestampSentAcknowledgement')),
            ('sentinsurance', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentInsurance')),
            ('sentwebsiteinfo', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentWebsiteInfo')),
            ('sentattire', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentAttire')),
            ('sentmedicial', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentMedicial')),
            ('sentfinance', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentFinance')),
            ('sentsecurityandsafety', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentSecurityAndSafety')),
            ('sentbiblereading', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentBibleReading')),
            ('senttawelcome', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentTAWelcome')),
            ('sentarrivalinstructions', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentArrivalInstructions')),
            ('sentbrodenniswelcome', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentBroDennisWelcome')),
            ('sentmentor', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentMentor')),
            ('sentbooks', self.gf('django.db.models.fields.CharField')(max_length=3L, db_column=u'sentBooks')),
        ))
        db.send_create_signal(u'migrate', ['Newapplicationsstatus'])

        # Adding model 'Notesexception'
        db.create_table(u'notesException', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('scheduleeventid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Scheduleevent'], db_column=u'scheduleEventID')),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'migrate', ['Notesexception'])

        # Adding model 'Notesreceived'
        db.create_table(u'notesReceived', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('rolleventid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Rollevent'], db_column=u'rollEventID')),
        ))
        db.send_create_signal(u'migrate', ['Notesreceived'])

        # Adding model 'Page'
        db.create_table(u'page', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('showinmenu', self.gf('django.db.models.fields.IntegerField')(db_column=u'showInMenu')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], null=True, db_column=u'userID', blank=True)),
            ('referrerid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'referrerID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Page'])

        # Adding model 'Pageaccounttype'
        db.create_table(u'pageAccountType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('pageid', self.gf('django.db.models.fields.IntegerField')(db_column=u'pageID')),
            ('accounttypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'accountTypeID')),
        ))
        db.send_create_signal(u'migrate', ['Pageaccounttype'])

        # Adding model 'Period'
        db.create_table(u'period', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('termid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Term'], db_column=u'termID')),
            ('periodnumber', self.gf('django.db.models.fields.IntegerField')(db_column=u'periodNumber')),
            ('startdate', self.gf('django.db.models.fields.DateField')(db_column=u'startDate')),
            ('enddate', self.gf('django.db.models.fields.DateField')(db_column=u'endDate')),
        ))
        db.send_create_signal(u'migrate', ['Period'])

        # Adding model 'QuestionEssays'
        db.create_table(u'question_essays', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('promptid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'promptID', blank=True)),
            ('essay', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('termid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'termID', blank=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'traineeID', blank=True)),
            ('avclassid', self.gf('django.db.models.fields.IntegerField')(db_column=u'avClassID')),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'migrate', ['QuestionEssays'])

        # Adding model 'QuestionPrompts'
        db.create_table(u'question_prompts', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=5000L)),
            ('termid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'termID', blank=True)),
            ('avclassid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'avClassID', blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mid_final', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['QuestionPrompts'])

        # Adding model 'Recentupdates'
        db.create_table(u'recentUpdates', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('timestamp', self.gf('django.db.models.fields.CharField')(max_length=64L)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Recentupdates'])

        # Adding model 'Recoveryweekday'
        db.create_table(u'recoveryWeekDay', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10L)),
        ))
        db.send_create_signal(u'migrate', ['Recoveryweekday'])

        # Adding model 'Reportcolumn'
        db.create_table(u'reportColumn', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('displayorder', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'displayOrder', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Reportcolumn'])

        # Adding model 'Reportcolumnquery'
        db.create_table(u'reportColumnQuery', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('reportcolumnid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Reportcolumn'], db_column=u'reportColumnID')),
            ('reportqueryid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Reportquery'], db_column=u'reportQueryID')),
        ))
        db.send_create_signal(u'migrate', ['Reportcolumnquery'])

        # Adding model 'Reportquery'
        db.create_table(u'reportQuery', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('query', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Reportquery'])

        # Adding model 'Requestcomment'
        db.create_table(u'requestComment', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('requestid', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'requestID')),
            ('dateentered', self.gf('django.db.models.fields.DateField')(db_column=u'dateEntered')),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Requestcomment'])

        # Adding model 'Requesttracking'
        db.create_table(u'requestTracking', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('startdate', self.gf('django.db.models.fields.DateField')(db_column=u'startDate')),
            ('actualenddate', self.gf('django.db.models.fields.DateField')(db_column=u'actualEndDate')),
            ('proposedenddate', self.gf('django.db.models.fields.DateField')(db_column=u'proposedEndDate')),
            ('assignedto', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'assignedTo')),
            ('requester', self.gf('django.db.models.fields.CharField')(max_length=50L)),
        ))
        db.send_create_signal(u'migrate', ['Requesttracking'])

        # Adding model 'Residence'
        db.create_table(u'residence', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('residencetypeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'residenceTypeID', blank=True)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
            ('streetaddress', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'streetAddress', blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2L, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'zipCode', blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=24L, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('reportseq', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'reportSeq', blank=True)),
            ('fttause', self.gf('django.db.models.fields.IntegerField')(db_column=u'fttaUse')),
            ('entrycode', self.gf('django.db.models.fields.CharField')(max_length=11L, db_column=u'entryCode', blank=True)),
            ('availablebeds', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'availableBeds', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Residence'])

        # Adding model 'Residencetype'
        db.create_table(u'residenceType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('residencetype', self.gf('django.db.models.fields.CharField')(max_length=5L, db_column=u'residenceType')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
        ))
        db.send_create_signal(u'migrate', ['Residencetype'])

        # Adding model 'ResidenceRepairs'
        db.create_table(u'residence_repairs', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('section_id', self.gf('django.db.models.fields.IntegerField')()),
            ('room_id', self.gf('django.db.models.fields.IntegerField')()),
            ('other_room', self.gf('django.db.models.fields.TextField')()),
            ('residence_id', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('trainee_id', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('completed', self.gf('django.db.models.fields.IntegerField')()),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['ResidenceRepairs'])

        # Adding model 'ResidenceRoomSections'
        db.create_table(u'residence_room_sections', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
        ))
        db.send_create_signal(u'migrate', ['ResidenceRoomSections'])

        # Adding model 'ResidenceRooms'
        db.create_table(u'residence_rooms', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
        ))
        db.send_create_signal(u'migrate', ['ResidenceRooms'])

        # Adding model 'Rolldata'
        db.create_table(u'rollData', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('rolleventid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Rollevent'], db_column=u'rollEventID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('rollstatusid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Rollstatus'], db_column=u'rollStatusID')),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('enteredbyuserid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], null=True, db_column=u'enteredByUserID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Rolldata'])

        # Adding model 'Rollevent'
        db.create_table(u'rollEvent', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('scheduleeventid', self.gf('django.db.models.fields.IntegerField')(db_column=u'scheduleEventID')),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Rollevent'])

        # Adding model 'Rollstatus'
        db.create_table(u'rollStatus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3L)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15L)),
        ))
        db.send_create_signal(u'migrate', ['Rollstatus'])

        # Adding model 'Rollhousefinalization'
        db.create_table(u'rollhousefinalization', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'residenceID')),
            ('submitdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submitDate')),
            ('weekstartdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'weekStartDate')),
            ('weekenddate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'weekEndDate')),
        ))
        db.send_create_signal(u'migrate', ['Rollhousefinalization'])

        # Adding model 'Rollsubmissiondata'
        db.create_table(u'rollsubmissiondata', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('submitdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submitDate')),
            ('startdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'startDate')),
            ('enddate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'endDate')),
        ))
        db.send_create_signal(u'migrate', ['Rollsubmissiondata'])

        # Adding model 'Rollteamfinalization'
        db.create_table(u'rollteamfinalization', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('teamid', self.gf('django.db.models.fields.IntegerField')(db_column=u'teamID')),
            ('submitdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submitDate')),
            ('weekstartdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'weekStartDate')),
            ('weekenddate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'weekEndDate')),
        ))
        db.send_create_signal(u'migrate', ['Rollteamfinalization'])

        # Adding model 'Rollypcfinalization'
        db.create_table(u'rollypcfinalization', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('submitdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submitDate')),
            ('weekstartdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'weekStartDate')),
            ('weekenddate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'weekEndDate')),
        ))
        db.send_create_signal(u'migrate', ['Rollypcfinalization'])

        # Adding model 'Room'
        db.create_table(u'room', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'residenceID')),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Room'])

        # Adding model 'Roomlist'
        db.create_table(u'roomlist', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1L)),
        ))
        db.send_create_signal(u'migrate', ['Roomlist'])

        # Adding model 'Roomreservationrequests'
        db.create_table(u'roomreservationrequests', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=11L)),
            ('groupsize', self.gf('django.db.models.fields.IntegerField')(db_column=u'groupSize')),
            ('frequency', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('starttime', self.gf('django.db.models.fields.TextField')(db_column=u'startTime')),
            ('endtime', self.gf('django.db.models.fields.TextField')(db_column=u'endTime')),
            ('duration', self.gf('django.db.models.fields.FloatField')()),
            ('reason', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('reminderflag', self.gf('django.db.models.fields.IntegerField')(db_column=u'reminderFlag')),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('fellowshipwith', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'fellowshipWith', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Roomreservationrequests'])

        # Adding model 'Roomschedule'
        db.create_table(u'roomschedule', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('roomid', self.gf('django.db.models.fields.IntegerField')(db_column=u'roomID')),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=255L)),
        ))
        db.send_create_signal(u'migrate', ['Roomschedule'])

        # Adding model 'RsMinistrybooks'
        db.create_table(u'rs_ministryBooks', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('cartnumber', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'cartNumber', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['RsMinistrybooks'])

        # Adding model 'RsSyllabus'
        db.create_table(u'rs_syllabus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('trainingclassesid', self.gf('django.db.models.fields.IntegerField')(db_column=u'trainingClassesID')),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('topic', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('classtype', self.gf('django.db.models.fields.CharField')(max_length=8L, db_column=u'classType')),
        ))
        db.send_create_signal(u'migrate', ['RsSyllabus'])

        # Adding model 'RsSyllabusreadings'
        db.create_table(u'rs_syllabusReadings', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('rs_syllabusid', self.gf('django.db.models.fields.IntegerField')(db_column=u'rs_syllabusID')),
            ('rs_ministrybooksid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'rs_ministrybooksID', blank=True)),
            ('readings', self.gf('django.db.models.fields.CharField')(max_length=255L)),
        ))
        db.send_create_signal(u'migrate', ['RsSyllabusreadings'])

        # Adding model 'Savedreport'
        db.create_table(u'savedReport', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
        ))
        db.send_create_signal(u'migrate', ['Savedreport'])

        # Adding model 'Savedreportcolumn'
        db.create_table(u'savedReportColumn', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('savedreportid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Savedreport'], db_column=u'savedReportID')),
            ('reportcolumnid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Reportcolumn'], db_column=u'reportColumnID')),
        ))
        db.send_create_signal(u'migrate', ['Savedreportcolumn'])

        # Adding model 'Schedule'
        db.create_table(u'schedule', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('startdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'startDate', blank=True)),
            ('enddate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'endDate', blank=True)),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('schedulecategoryid', self.gf('django.db.models.fields.IntegerField')(db_column=u'scheduleCategoryID')),
            ('priority', self.gf('django.db.models.fields.BigIntegerField')()),
            ('accounttypeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Accounttype'], null=True, db_column=u'accountTypeID', blank=True)),
            ('display', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Schedule'])

        # Adding model 'Schedulecategory'
        db.create_table(u'scheduleCategory', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
        ))
        db.send_create_signal(u'migrate', ['Schedulecategory'])

        # Adding model 'Scheduleevent'
        db.create_table(u'scheduleEvent', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('scheduleid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Schedule'], db_column=u'scheduleID')),
            ('weekdayid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Weekday'], db_column=u'weekDayID')),
            ('starttime', self.gf('django.db.models.fields.TextField')(db_column=u'startTime')),
            ('endtime', self.gf('django.db.models.fields.TextField')(db_column=u'endTime')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('isclass', self.gf('django.db.models.fields.IntegerField')(db_column=u'isClass')),
            ('isroll', self.gf('django.db.models.fields.IntegerField')(db_column=u'isRoll')),
        ))
        db.send_create_signal(u'migrate', ['Scheduleevent'])

        # Adding model 'Scheduletraineefilter'
        db.create_table(u'scheduleTraineeFilter', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('scheduleid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Schedule'], db_column=u'scheduleID')),
            ('traineefilterid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Traineefilter'], db_column=u'traineeFilterID')),
        ))
        db.send_create_signal(u'migrate', ['Scheduletraineefilter'])

        # Adding model 'Seat'
        db.create_table(u'seat', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('seatx', self.gf('django.db.models.fields.IntegerField')(db_column=u'seatX')),
            ('seaty', self.gf('django.db.models.fields.IntegerField')(db_column=u'seatY')),
            ('seatingchartid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Seatingchart'], db_column=u'seatingChartID')),
        ))
        db.send_create_signal(u'migrate', ['Seat'])

        # Adding model 'Seating'
        db.create_table(u'seating', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('seatid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Seat'], db_column=u'seatID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], null=True, db_column=u'traineeID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Seating'])

        # Adding model 'Seatingchart'
        db.create_table(u'seatingChart', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('seatingchartname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50L, db_column=u'seatingChartName')),
        ))
        db.send_create_signal(u'migrate', ['Seatingchart'])

        # Adding model 'Seatingevent'
        db.create_table(u'seatingEvent', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('seatingchartid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Seatingchart'], db_column=u'seatingChartID')),
            ('scheduleeventid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Scheduleevent'], db_column=u'scheduleEventID')),
        ))
        db.send_create_signal(u'migrate', ['Seatingevent'])

        # Adding model 'Semiannualstudyattendance'
        db.create_table(u'semiAnnualStudyAttendance', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('d1', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('d2', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('d3', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('d4', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('d5', self.gf('django.db.models.fields.CharField')(max_length=1L)),
        ))
        db.send_create_signal(u'migrate', ['Semiannualstudyattendance'])

        # Adding model 'Semiannualstudylocation'
        db.create_table(u'semiAnnualStudyLocation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Semiannualstudylocation'])

        # Adding model 'Semiannualtesting'
        db.create_table(u'semiAnnualTesting', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('groupnumber', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'groupNumber', blank=True)),
            ('servicecode', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'serviceCode', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Semiannualtesting'])

        # Adding model 'Semiannualtestingrooms'
        db.create_table(u'semiAnnualTestingRooms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupnumber', self.gf('django.db.models.fields.IntegerField')(db_column=u'groupNumber')),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('room', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Semiannualtestingrooms'])

        # Adding model 'Sendinglocality'
        db.create_table(u'sendingLocality', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('localityid', self.gf('django.db.models.fields.IntegerField')(db_column=u'localityID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
        ))
        db.send_create_signal(u'migrate', ['Sendinglocality'])

        # Adding model 'Svassignment'
        db.create_table(u'svAssignment', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('svserviceworkergroupid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svserviceworkergroup'], db_column=u'svServiceWorkerGroupID')),
            ('svscheduleinstanceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svscheduleinstance'], db_column=u'svScheduleInstanceID')),
        ))
        db.send_create_signal(u'migrate', ['Svassignment'])

        # Adding model 'Svassignmentsave'
        db.create_table(u'svAssignmentSave', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('svserviceworkergroupid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceWorkerGroupID')),
            ('svscheduleinstanceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svScheduleInstanceID')),
        ))
        db.send_create_signal(u'migrate', ['Svassignmentsave'])

        # Adding model 'Svexception'
        db.create_table(u'svException', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('startdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'startDate', blank=True)),
            ('enddate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'endDate', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svexception'])

        # Adding model 'Svexceptionservice'
        db.create_table(u'svExceptionService', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('svexceptionid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svExceptionID', blank=True)),
            ('svserviceid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svServiceID', blank=True)),
            ('svservicescheduleid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svServiceScheduleID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svexceptionservice'])

        # Adding model 'Svexceptiontrainee'
        db.create_table(u'svExceptionTrainee', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('svexceptionid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svExceptionID', blank=True)),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'traineeID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svexceptiontrainee'])

        # Adding model 'Svmissedservice'
        db.create_table(u'svMissedService', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('svscheduleinstanceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svScheduleInstanceID')),
            ('svserviceworkergroupid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceWorkerGroupID')),
        ))
        db.send_create_signal(u'migrate', ['Svmissedservice'])

        # Adding model 'Svnote'
        db.create_table(u'svNote', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('data', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('norder', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], null=True, db_column=u'userID', blank=True)),
            ('moddate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'modDate')),
        ))
        db.send_create_signal(u'migrate', ['Svnote'])

        # Adding model 'Svpermanentassignment'
        db.create_table(u'svPermanentAssignment', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('svserviceworkergroupid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svserviceworkergroup'], db_column=u'svServiceWorkerGroupID')),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Svpermanentassignment'])

        # Adding model 'Svqualificationgroup'
        db.create_table(u'svQualificationGroup', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('traineefilterid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Traineefilter'], db_column=u'traineeFilterID')),
        ))
        db.send_create_signal(u'migrate', ['Svqualificationgroup'])

        # Adding model 'Svreport'
        db.create_table(u'svReport', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('headermessage', self.gf('django.db.models.fields.TextField')(db_column=u'headerMessage', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svreport'])

        # Adding model 'Svreportnote'
        db.create_table(u'svReportNote', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('reporttype', self.gf('django.db.models.fields.CharField')(max_length=511L, db_column=u'reportType', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svreportnote'])

        # Adding model 'Svreportservice'
        db.create_table(u'svReportService', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svreportid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svReportID')),
            ('svserviceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceID')),
            ('sortorder', self.gf('django.db.models.fields.IntegerField')(db_column=u'sortOrder')),
        ))
        db.send_create_signal(u'migrate', ['Svreportservice'])

        # Adding model 'Svreporttraineecomment'
        db.create_table(u'svReportTraineeComment', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svscheduleinstanceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svscheduleinstance'], db_column=u'svScheduleInstanceID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svreporttraineecomment'])

        # Adding model 'Svrolldata'
        db.create_table(u'svRollData', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svrolleventid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svrollevent'], db_column=u'svRollEventID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('substitutetraineeid', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'svrolldata+', db_column=u'substituteTraineeID', to=orm['migrate.Trainee'])),
            ('isvolunteer', self.gf('django.db.models.fields.IntegerField')(db_column=u'isVolunteer')),
            ('rollstatusid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Rollstatus'], db_column=u'rollStatusID')),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=45L)),
        ))
        db.send_create_signal(u'migrate', ['Svrolldata'])

        # Adding model 'Svrollevent'
        db.create_table(u'svRollEvent', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], db_column=u'userID')),
            ('svservicetimeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svservicetime'], db_column=u'svServiceTimeID')),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=45L)),
        ))
        db.send_create_signal(u'migrate', ['Svrollevent'])

        # Adding model 'Svscheduleinstance'
        db.create_table(u'svScheduleInstance', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], null=True, db_column=u'userID', blank=True)),
            ('svservicescheduleid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceScheduleID')),
            ('startdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'startDate', blank=True)),
            ('modifiedtime', self.gf('django.db.models.fields.DateTimeField')(db_column=u'modifiedTime')),
        ))
        db.send_create_signal(u'migrate', ['Svscheduleinstance'])

        # Adding model 'Svservice'
        db.create_table(u'svService', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('isactive', self.gf('django.db.models.fields.IntegerField')(db_column=u'isActive')),
            ('svservicecategoryid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svservicecategory'], db_column=u'svServiceCategoryID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('svservicesorttypeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svservicesorttype'], db_column=u'svServiceSortTypeID')),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'migrate', ['Svservice'])

        # Adding model 'Svservicealgorithm'
        db.create_table(u'svServiceAlgorithm', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svservicesorttypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceSortTypeID')),
            ('emphasis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'migrate', ['Svservicealgorithm'])

        # Adding model 'Svservicecategory'
        db.create_table(u'svServiceCategory', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Svservicecategory'])

        # Adding model 'Svserviceschedule'
        db.create_table(u'svServiceSchedule', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svserviceschedule'])

        # Adding model 'Svservicesorttype'
        db.create_table(u'svServiceSortType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3L)),
        ))
        db.send_create_signal(u'migrate', ['Svservicesorttype'])

        # Adding model 'Svservicetime'
        db.create_table(u'svServiceTime', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svserviceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svservice'], db_column=u'svServiceID')),
            ('svservicescheduleid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceScheduleID')),
            ('week', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('weekdayid', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'svservicetime+', db_column=u'weekDayID', to=orm['migrate.Weekday'])),
            ('starttime', self.gf('django.db.models.fields.TextField')(db_column=u'startTime')),
            ('endtime', self.gf('django.db.models.fields.TextField')(db_column=u'endTime', blank=True)),
            ('weekdayid2', self.gf('django.db.models.fields.IntegerField')(db_column=u'weekDayID2')),
            ('starttime2', self.gf('django.db.models.fields.TextField')(db_column=u'startTime2')),
            ('endtime2', self.gf('django.db.models.fields.TextField')(db_column=u'endTime2', blank=True)),
            ('hidden_value2', self.gf('django.db.models.fields.IntegerField')()),
            ('weekdayid3', self.gf('django.db.models.fields.IntegerField')(db_column=u'weekDayID3')),
            ('starttime3', self.gf('django.db.models.fields.TextField')(db_column=u'startTime3')),
            ('endtime3', self.gf('django.db.models.fields.TextField')(db_column=u'endTime3', blank=True)),
            ('hidden_value3', self.gf('django.db.models.fields.IntegerField')()),
            ('recoveryweekdayid', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'svservicetime', db_column=u'recoveryWeekDayID', to=orm['migrate.Weekday'])),
            ('recoverytime', self.gf('django.db.models.fields.TextField')(db_column=u'recoveryTime', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svservicetime'])

        # Adding model 'Svservicetimescheduleevent'
        db.create_table(u'svServiceTimeScheduleEvent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('svservicetimeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceTimeID')),
            ('scheduleeventid', self.gf('django.db.models.fields.IntegerField')(db_column=u'scheduleEventID')),
        ))
        db.send_create_signal(u'migrate', ['Svservicetimescheduleevent'])

        # Adding model 'Svservicetoschedulemap'
        db.create_table(u'svServiceToScheduleMap', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svservicescheduleid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceScheduleID')),
            ('svserviceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceID')),
        ))
        db.send_create_signal(u'migrate', ['Svservicetoschedulemap'])

        # Adding model 'Svservicetraineefilter'
        db.create_table(u'svServiceTraineeFilter', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svserviceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svservice'], db_column=u'svServiceID')),
            ('traineefilterid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Traineefilter'], db_column=u'traineeFilterID')),
        ))
        db.send_create_signal(u'migrate', ['Svservicetraineefilter'])

        # Adding model 'Svserviceweeklyreport'
        db.create_table(u'svServiceWeeklyReport', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('svserviceid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceID')),
            ('weekid', self.gf('django.db.models.fields.IntegerField')(db_column=u'weekID')),
            ('termid', self.gf('django.db.models.fields.IntegerField')(db_column=u'termID')),
            ('lastupdate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'lastUpdate')),
        ))
        db.send_create_signal(u'migrate', ['Svserviceweeklyreport'])

        # Adding model 'Svserviceweeklyreportentry'
        db.create_table(u'svServiceWeeklyReportEntry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svserviceweeklyreportid', self.gf('django.db.models.fields.IntegerField')(db_column=u'svServiceWeeklyReportID')),
            ('dayid', self.gf('django.db.models.fields.IntegerField')(db_column=u'dayID')),
            ('starttime', self.gf('django.db.models.fields.TextField')(db_column=u'startTime', blank=True)),
            ('endtime', self.gf('django.db.models.fields.TextField')(db_column=u'endTime', blank=True)),
            ('taskperformed', self.gf('django.db.models.fields.TextField')(db_column=u'taskPerformed', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svserviceweeklyreportentry'])

        # Adding model 'Svserviceworkergroup'
        db.create_table(u'svServiceWorkerGroup', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('svserviceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svservice'], db_column=u'svServiceID')),
            ('numberofworkers', self.gf('django.db.models.fields.IntegerField')(db_column=u'numberOfWorkers')),
            ('isactive', self.gf('django.db.models.fields.IntegerField')(db_column=u'isActive')),
            ('svservicescheduleid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svServiceScheduleID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svserviceworkergroup'])

        # Adding model 'Svserviceworkergroupsnapshot'
        db.create_table(u'svServiceWorkerGroupSnapshot', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svscheduleinstanceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svscheduleinstance'], db_column=u'svScheduleInstanceID')),
            ('svserviceworkergroupid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svserviceworkergroup'], db_column=u'svServiceWorkerGroupID')),
            ('numberofworkers', self.gf('django.db.models.fields.IntegerField')(db_column=u'numberOfWorkers')),
        ))
        db.send_create_signal(u'migrate', ['Svserviceworkergroupsnapshot'])

        # Adding model 'Svserviceworkergrouptraineefilter'
        db.create_table(u'svServiceWorkerGroupTraineeFilter', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('svserviceworkergroupid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svserviceworkergroup'], db_column=u'svServiceWorkerGroupID')),
            ('traineefilterid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Traineefilter'], db_column=u'traineeFilterID')),
        ))
        db.send_create_signal(u'migrate', ['Svserviceworkergrouptraineefilter'])

        # Adding model 'Svworkerexception'
        db.create_table(u'svWorkerException', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('svserviceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svservice'], null=True, db_column=u'svServiceID', blank=True)),
            ('startdate', self.gf('django.db.models.fields.DateField')(db_column=u'startDate')),
            ('enddate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'endDate', blank=True)),
            ('reason', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svworkerexception'])

        # Adding model 'Svworkerqualification'
        db.create_table(u'svWorkerQualification', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainee'], db_column=u'traineeID')),
            ('svqualificationgroupid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Svqualificationgroup'], db_column=u'svQualificationGroupID')),
        ))
        db.send_create_signal(u'migrate', ['Svworkerqualification'])

        # Adding model 'Svworkloadhistory'
        db.create_table(u'svWorkloadHistory', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('oldworkload', self.gf('django.db.models.fields.IntegerField')(db_column=u'oldWorkload')),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'migrate', ['Svworkloadhistory'])

        # Adding model 'Svserviceview'
        db.create_table(u'svserviceview', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('isactive', self.gf('django.db.models.fields.IntegerField')(db_column=u'isActive')),
            ('categoryid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'categoryID', blank=True)),
            ('categoryname', self.gf('django.db.models.fields.CharField')(max_length=45L, db_column=u'categoryName', blank=True)),
            ('servicefilterlookupid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'serviceFilterLookupID', blank=True)),
            ('servicefilterid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'serviceFilterID', blank=True)),
            ('servicefiltername', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'serviceFilterName', blank=True)),
            ('workergrpid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'workerGrpID', blank=True)),
            ('workergrpname', self.gf('django.db.models.fields.CharField')(max_length=45L, db_column=u'workerGrpName', blank=True)),
            ('workergrpsuffix', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'workerGrpSuffix', blank=True)),
            ('workergrpisactive', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'workerGrpIsActive', blank=True)),
            ('workergrpfilterlookupid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'workerGrpFilterLookupID', blank=True)),
            ('workergrpfilterid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'workerGrpFilterID', blank=True)),
            ('workergrpfiltername', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'workerGrpFilterName', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Svserviceview'])

        # Adding model 'Team'
        db.create_table(u'team', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('teamtypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'teamTypeID')),
            ('trainerusername', self.gf('django.db.models.fields.CharField')(max_length=45L, db_column=u'trainerUserName')),
            ('bromonitortraineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'broMonitorTraineeID')),
            ('sismonitortraineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'sisMonitorTraineeID')),
        ))
        db.send_create_signal(u'migrate', ['Team'])

        # Adding model 'Teamschedule'
        db.create_table(u'teamSchedule', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('teamid', self.gf('django.db.models.fields.IntegerField')(db_column=u'teamID')),
            ('scheduleid', self.gf('django.db.models.fields.IntegerField')(db_column=u'scheduleID')),
        ))
        db.send_create_signal(u'migrate', ['Teamschedule'])

        # Adding model 'Teamtype'
        db.create_table(u'teamType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100L)),
        ))
        db.send_create_signal(u'migrate', ['Teamtype'])

        # Adding model 'Term'
        db.create_table(u'term', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45L)),
            ('startdate', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'startDate')),
            ('enddate', self.gf('django.db.models.fields.CharField')(max_length=10L, db_column=u'endDate')),
            ('taskstage', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'taskStage', blank=True)),
            ('taskscompleted', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'tasksCompleted', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Term'])

        # Adding model 'Tmplsimportoffense'
        db.create_table(u'tmpLsImportOffense', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('lastfirst', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'lastFirst')),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=7L)),
            ('offensereason', self.gf('django.db.models.fields.CharField')(max_length=30L, db_column=u'offenseReason')),
            ('numlsowed', self.gf('django.db.models.fields.IntegerField')(db_column=u'numLSOwed')),
            ('manualhandling', self.gf('django.db.models.fields.IntegerField')(db_column=u'manualHandling')),
            ('importsignedin', self.gf('django.db.models.fields.IntegerField')(db_column=u'importSignedIn')),
            ('fullyturnedin', self.gf('django.db.models.fields.IntegerField')(db_column=u'FullyTurnedIn')),
            ('dns', self.gf('django.db.models.fields.IntegerField')(db_column=u'DNS')),
            ('wnr', self.gf('django.db.models.fields.IntegerField')(db_column=u'WNR')),
            ('snc', self.gf('django.db.models.fields.IntegerField')(db_column=u'SNC')),
            ('numlsreceived', self.gf('django.db.models.fields.IntegerField')(db_column=u'numLSReceived')),
            ('lastupdatedate', self.gf('django.db.models.fields.DateField')(db_column=u'lastUpdateDate')),
            ('datedue', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'DateDue', blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Tmplsimportoffense'])

        # Adding model 'Trainee'
        db.create_table(u'trainee', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'trainee+', null=True, db_column=u'userID', to=orm['migrate.User'], blank=True, unique=True)),
            ('datebegin', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dateBegin', blank=True)),
            ('dateend', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dateEnd', blank=True)),
            ('firstterm_termid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Term'], null=True, db_column=u'firstTerm_termID', blank=True)),
            ('secondterm_termid', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'trainee+', null=True, db_column=u'secondTerm_termID', to=orm['migrate.Term'])),
            ('thirdterm_termid', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'trainee+', null=True, db_column=u'thirdTerm_termID', to=orm['migrate.Term'])),
            ('fourthterm_termid', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'trainee+', null=True, db_column=u'fourthTerm_termID', to=orm['migrate.Term'])),
            ('termscompleted', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'termsCompleted', blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('couple', self.gf('django.db.models.fields.IntegerField')()),
            ('emergencycontact', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'emergencyContact', blank=True)),
            ('emergencyaddress', self.gf('django.db.models.fields.TextField')(db_column=u'emergencyAddress', blank=True)),
            ('emergencyphonenumber', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'emergencyPhoneNumber', blank=True)),
            ('emergencyphonenumber2', self.gf('django.db.models.fields.CharField')(max_length=14L, db_column=u'emergencyPhoneNumber2', blank=True)),
            ('readoldtestament', self.gf('django.db.models.fields.IntegerField')(db_column=u'readOldTestament')),
            ('readnewtestament', self.gf('django.db.models.fields.IntegerField')(db_column=u'readNewTestament')),
            ('trainingassistantid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Trainingassistant'], null=True, db_column=u'trainingAssistantID', blank=True)),
            ('mentor_userid', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'trainee', null=True, db_column=u'mentor_userID', to=orm['migrate.User'])),
            ('mentor', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('college', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('degree', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gospelpreference1', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'gospelPreference1', blank=True)),
            ('gospelpreference2', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'gospelPreference2', blank=True)),
            ('vehicleinfoold', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleInfoOld', blank=True)),
            ('vehiclemakeold', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'vehicleMakeOld', blank=True)),
            ('vehiclemodelold', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'vehicleModelOld', blank=True)),
            ('vehicleyearold', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'vehicleYearOld', blank=True)),
            ('vehicleyesno', self.gf('django.db.models.fields.IntegerField')(db_column=u'vehicleYesNo')),
            ('vehiclemodel', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleModel', blank=True)),
            ('vehiclelicense', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleLicense', blank=True)),
            ('vehiclecolor', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleColor', blank=True)),
            ('vehiclecapacity', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'vehicleCapacity', blank=True)),
            ('teamid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'teamID', blank=True)),
            ('residenceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Residence'], null=True, db_column=u'residenceID', blank=True)),
            ('greekcharacter', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('svservicesleft', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svServicesLeft', blank=True)),
            ('officeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'officeID', blank=True)),
            ('traineestatusid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Traineestatus'], db_column=u'traineeStatusID')),
            ('bunkid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'bunkID', blank=True)),
            ('mrtype', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MRType', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Trainee'])

        # Adding model 'Traineefilter'
        db.create_table(u'traineeFilter', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('filter', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Traineefilter'])

        # Adding model 'Traineeschedule'
        db.create_table(u'traineeSchedule', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeID')),
            ('scheduleid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Schedule'], db_column=u'scheduleID')),
            ('startdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'startDate', blank=True)),
            ('enddate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'endDate', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Traineeschedule'])

        # Adding model 'Traineestatus'
        db.create_table(u'traineeStatus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Traineestatus'])

        # Adding model 'TraineeOld'
        db.create_table(u'trainee_old', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, db_column=u'userID', blank=True)),
            ('lastname', self.gf('django.db.models.fields.TextField')(db_column=u'lastName')),
            ('firstname', self.gf('django.db.models.fields.TextField')(db_column=u'firstName')),
            ('middlename', self.gf('django.db.models.fields.TextField')(db_column=u'middleName', blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'birthDate', blank=True)),
            ('sendinglocality', self.gf('django.db.models.fields.TextField')(db_column=u'sendingLocality', blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('termscompleted', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'termsCompleted', blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('datebegin', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dateBegin', blank=True)),
            ('dateend', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dateEnd', blank=True)),
            ('maritalstatus', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'maritalStatus', blank=True)),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'residenceID', blank=True)),
            ('cellphone', self.gf('django.db.models.fields.CharField')(max_length=30L, db_column=u'cellPhone', blank=True)),
            ('teamid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'teamID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['TraineeOld'])

        # Adding model 'Traineeview'
        db.create_table(u'traineeview', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=65L)),
            ('lastfirst', self.gf('django.db.models.fields.CharField')(max_length=66L, db_column=u'lastFirst')),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'firstName')),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'lastName')),
            ('middlename', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'middleName', blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'birthDate', blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('traineestatusid', self.gf('django.db.models.fields.IntegerField')(db_column=u'traineeStatusID')),
            ('traineestatus', self.gf('django.db.models.fields.TextField')(db_column=u'traineeStatus', blank=True)),
            ('maritalstatus', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'maritalStatus', blank=True)),
            ('couple', self.gf('django.db.models.fields.IntegerField')()),
            ('greekcharacter', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('cellphone', self.gf('django.db.models.fields.CharField')(max_length=14L, db_column=u'cellPhone', blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=32L)),
            ('sendinglocality', self.gf('django.db.models.fields.TextField')(db_column=u'sendingLocality', blank=True)),
            ('termscompleted', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'termsCompleted', blank=True)),
            ('datebegin', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dateBegin', blank=True)),
            ('dateend', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'dateEnd', blank=True)),
            ('residenceid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'residenceID', blank=True)),
            ('residencename', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'residenceName', blank=True)),
            ('teamid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'teamID', blank=True)),
            ('teamname', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'teamName', blank=True)),
            ('teamcode', self.gf('django.db.models.fields.CharField')(max_length=15L, db_column=u'teamCode', blank=True)),
            ('teamtrainer', self.gf('django.db.models.fields.CharField')(max_length=45L, db_column=u'teamTrainer', blank=True)),
            ('svservicesleft', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'svServicesLeft', blank=True)),
            ('trainingassistantid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'trainingAssistantID', blank=True)),
            ('trainingassistantname', self.gf('django.db.models.fields.CharField')(max_length=65L, db_column=u'trainingAssistantName', blank=True)),
            ('vehicleinfo', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'vehicleInfo', blank=True)),
            ('vehiclemake', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleMake', blank=True)),
            ('vehiclemodel', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleModel', blank=True)),
            ('vehicleyear', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleYear', blank=True)),
            ('vehiclelicense', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleLicense', blank=True)),
            ('vehiclecolor', self.gf('django.db.models.fields.CharField')(max_length=50L, db_column=u'vehicleColor', blank=True)),
            ('vehiclecapacity', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'vehicleCapacity', blank=True)),
            ('teamtypeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'teamTypeID', blank=True)),
            ('teamtype', self.gf('django.db.models.fields.CharField')(max_length=100L, db_column=u'teamType', blank=True)),
            ('officeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'officeID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Traineeview'])

        # Adding model 'Trainingassistant'
        db.create_table(u'trainingAssistant', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], db_column=u'userID')),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'lastName')),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'firstName')),
            ('middlename', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'middleName', blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'birthDate', blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('maritalstatus', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'maritalStatus', blank=True)),
            ('residence', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('outoftown', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'outOfTown', blank=True)),
            ('approvingtaid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'approvingTAID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Trainingassistant'])

        # Adding model 'Trainingclasses'
        db.create_table(u'trainingClasses', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('weekdayid', self.gf('django.db.models.fields.IntegerField')(db_column=u'weekdayID')),
            ('readwhen', self.gf('django.db.models.fields.IntegerField')(db_column=u'readWhen')),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=6L)),
            ('hassyllabus', self.gf('django.db.models.fields.IntegerField')(db_column=u'hasSyllabus')),
            ('secode', self.gf('django.db.models.fields.TextField')(db_column=u'seCode')),
        ))
        db.send_create_signal(u'migrate', ['Trainingclasses'])

        # Adding model 'Trainingassistantview'
        db.create_table(u'trainingassistantview', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=65L)),
            ('lastfirst', self.gf('django.db.models.fields.CharField')(max_length=66L, db_column=u'lastFirst')),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'firstName')),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'lastName')),
            ('outoftown', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'outOfTown', blank=True)),
            ('approvingtaid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'approvingTAID', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Trainingassistantview'])

        # Adding model 'User'
        db.create_table(u'user', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32L)),
            ('encryptedpassword', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'encryptedPassword', blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'firstName')),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'nickName', blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'lastName')),
            ('middlename', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'middleName', blank=True)),
            ('maidenname', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'maidenName', blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, db_column=u'birthDate', blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('home_localityid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'home_localityID', blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10L, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('maritalstatus', self.gf('django.db.models.fields.CharField')(max_length=1L, db_column=u'maritalStatus', blank=True)),
            ('homephone', self.gf('django.db.models.fields.CharField')(max_length=14L, db_column=u'homePhone', blank=True)),
            ('cellphone', self.gf('django.db.models.fields.CharField')(max_length=14L, db_column=u'cellPhone', blank=True)),
            ('workphone', self.gf('django.db.models.fields.TextField')(db_column=u'workPhone', blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255L, blank=True)),
            ('lastlogin', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'lastLogin', blank=True)),
            ('lastip', self.gf('django.db.models.fields.CharField')(max_length=15L, db_column=u'lastIP', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['User'])

        # Adding model 'Useraccounttype'
        db.create_table(u'userAccountType', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.User'], db_column=u'userID')),
            ('accounttypeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['migrate.Accounttype'], db_column=u'accountTypeID')),
        ))
        db.send_create_signal(u'migrate', ['Useraccounttype'])

        # Adding model 'Waapprovalstatus'
        db.create_table(u'waApprovalStatus', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('approvalstatus', self.gf('django.db.models.fields.CharField')(max_length=12L, db_column=u'approvalStatus')),
        ))
        db.send_create_signal(u'migrate', ['Waapprovalstatus'])

        # Adding model 'Wamaclist'
        db.create_table(u'waMACList', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=17L)),
            ('userid', self.gf('django.db.models.fields.IntegerField')(db_column=u'userID')),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'migrate', ['Wamaclist'])

        # Adding model 'Wareason'
        db.create_table(u'waReason', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=32L)),
        ))
        db.send_create_signal(u'migrate', ['Wareason'])

        # Adding model 'Warequest'
        db.create_table(u'waRequest', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('traineeid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'traineeID', blank=True)),
            ('wareasonid', self.gf('django.db.models.fields.IntegerField')(db_column=u'waReasonID')),
            ('minutes', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('submissiondate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'submissionDate')),
            ('timestart', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=17L, db_column=u'MAC')),
            ('waapprovalstatusid', self.gf('django.db.models.fields.IntegerField')(db_column=u'waApprovalStatusID')),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('usagetime', self.gf('django.db.models.fields.TextField')(db_column=u'usageTime', blank=True)),
            ('usagedate', self.gf('django.db.models.fields.DateField')(db_column=u'usageDate')),
            ('tacomments', self.gf('django.db.models.fields.TextField')(db_column=u'TAComments', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Warequest'])

        # Adding model 'Weatherlocation'
        db.create_table(u'weatherLocation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32L)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5L)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=4, blank=True)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=4, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('cache', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Weatherlocation'])

        # Adding model 'Weekday'
        db.create_table(u'weekDay', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10L)),
            ('dayorder', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'dayOrder', blank=True)),
        ))
        db.send_create_signal(u'migrate', ['Weekday'])


    def backwards(self, orm):
        # Deleting model 'Hcrecmd'
        db.delete_table(u'HCRecmd')

        # Deleting model 'Hcrecmdcriteria'
        db.delete_table(u'HCRecmdCriteria')

        # Deleting model 'Accounttype'
        db.delete_table(u'accountType')

        # Deleting model 'Announcementmember'
        db.delete_table(u'announcementMember')

        # Deleting model 'Announcementrequest'
        db.delete_table(u'announcementRequest')

        # Deleting model 'Announcementselection'
        db.delete_table(u'announcementSelection')

        # Deleting model 'Announcementstatus'
        db.delete_table(u'announcementStatus')

        # Deleting model 'Announcementtype'
        db.delete_table(u'announcementType')

        # Deleting model 'Atrabsenttrainee'
        db.delete_table(u'atrAbsentTrainee')

        # Deleting model 'Atrroster'
        db.delete_table(u'atrRoster')

        # Deleting model 'Atrunreportedhouse'
        db.delete_table(u'atrUnreportedHouse')

        # Deleting model 'Attendancesystem'
        db.delete_table(u'attendancesystem')

        # Deleting model 'Attendancetables'
        db.delete_table(u'attendancetables')

        # Deleting model 'Avapprovalstatus'
        db.delete_table(u'avApprovalStatus')

        # Deleting model 'Avclass'
        db.delete_table(u'avClass')

        # Deleting model 'Avreason'
        db.delete_table(u'avReason')

        # Deleting model 'Avrequest'
        db.delete_table(u'avRequest')

        # Deleting model 'Avrequestcomment'
        db.delete_table(u'avRequestComment')

        # Deleting model 'Bostonapp'
        db.delete_table(u'bostonApp')

        # Deleting model 'BrBooks'
        db.delete_table(u'br_books')

        # Deleting model 'BrTraineeBook'
        db.delete_table(u'br_trainee_book')

        # Deleting model 'Bugs'
        db.delete_table(u'bugs')

        # Deleting model 'Bunk'
        db.delete_table(u'bunk')

        # Deleting model 'Church'
        db.delete_table(u'church')

        # Deleting model 'Classnotes'
        db.delete_table(u'classNotes')

        # Deleting model 'Conference'
        db.delete_table(u'conference')

        # Deleting model 'Dailybibleverse'
        db.delete_table(u'dailyBibleVerse')

        # Deleting model 'Dberror'
        db.delete_table(u'dbError')

        # Deleting model 'Exams'
        db.delete_table(u'exams')

        # Deleting model 'Examstraineeaccess'
        db.delete_table(u'examsTraineeAccess')

        # Deleting model 'Examstraineeanswers'
        db.delete_table(u'examsTraineeAnswers')

        # Deleting model 'Examstraineeanswersgrades'
        db.delete_table(u'examsTraineeAnswersGrades')

        # Deleting model 'FrameRequests'
        db.delete_table(u'frame_requests')

        # Deleting model 'Globalsettings'
        db.delete_table(u'globalSettings')

        # Deleting model 'Gospelcitizenship'
        db.delete_table(u'gospelCitizenship')

        # Deleting model 'Gospelsurvey'
        db.delete_table(u'gospelSurvey')

        # Deleting model 'Gospeltripapplication'
        db.delete_table(u'gospelTripApplication')

        # Deleting model 'Gospeltriparrangement'
        db.delete_table(u'gospelTripArrangement')

        # Deleting model 'Gospeltripassignment'
        db.delete_table(u'gospelTripAssignment')

        # Deleting model 'Gospeltripdestination'
        db.delete_table(u'gospelTripDestination')

        # Deleting model 'Gospeltripdriver'
        db.delete_table(u'gospelTripDriver')

        # Deleting model 'Gospeltripflight'
        db.delete_table(u'gospelTripFlight')

        # Deleting model 'Gospeltripinformation'
        db.delete_table(u'gospelTripInformation')

        # Deleting model 'Gospeltriplanguage'
        db.delete_table(u'gospelTripLanguage')

        # Deleting model 'Gospeltripoverseer'
        db.delete_table(u'gospelTripOverseer')

        # Deleting model 'Gospeltrippassport'
        db.delete_table(u'gospelTripPassport')

        # Deleting model 'Gospeltrippayment'
        db.delete_table(u'gospelTripPayment')

        # Deleting model 'Gospeltripproficiency'
        db.delete_table(u'gospelTripProficiency')

        # Deleting model 'Gospeltriprun'
        db.delete_table(u'gospelTripRun')

        # Deleting model 'Gospeltriprundriver'
        db.delete_table(u'gospelTripRunDriver')

        # Deleting model 'Gospeltripselection'
        db.delete_table(u'gospelTripSelection')

        # Deleting model 'Gospeltripvehicle'
        db.delete_table(u'gospelTripVehicle')

        # Deleting model 'Gospeltype'
        db.delete_table(u'gospelType')

        # Deleting model 'Gp'
        db.delete_table(u'gp')

        # Deleting model 'Gpstats'
        db.delete_table(u'gpStats')

        # Deleting model 'Gpteam'
        db.delete_table(u'gpTeam')

        # Deleting model 'Gptype'
        db.delete_table(u'gpType')

        # Deleting model 'GradActivity'
        db.delete_table(u'grad_activity')

        # Deleting model 'GradAdmin'
        db.delete_table(u'grad_admin')

        # Deleting model 'GradConsiderations'
        db.delete_table(u'grad_considerations')

        # Deleting model 'GradInvites'
        db.delete_table(u'grad_invites')

        # Deleting model 'GradRemembrance'
        db.delete_table(u'grad_remembrance')

        # Deleting model 'GradSpeaking'
        db.delete_table(u'grad_speaking')

        # Deleting model 'GradStats'
        db.delete_table(u'grad_stats')

        # Deleting model 'GradSurvey'
        db.delete_table(u'grad_survey')

        # Deleting model 'GradTestimony'
        db.delete_table(u'grad_testimony')

        # Deleting model 'Greekparsing'
        db.delete_table(u'greekParsing')

        # Deleting model 'Greekuserstats'
        db.delete_table(u'greekUserStats')

        # Deleting model 'Greekvocab'
        db.delete_table(u'greekVocab')

        # Deleting model 'Gtcasurvey'
        db.delete_table(u'gtcaSurvey')

        # Deleting model 'Hcsurvey'
        db.delete_table(u'hcSurvey')

        # Deleting model 'Hcsurveytraineenotes'
        db.delete_table(u'hcSurveyTraineeNotes')

        # Deleting model 'Hcrecmdqs'
        db.delete_table(u'hcrecmdqs')

        # Deleting model 'Houseinspectionfaq'
        db.delete_table(u'houseInspectionFAQ')

        # Deleting model 'Importsql'
        db.delete_table(u'importSQL')

        # Deleting model 'Importsqlauthor'
        db.delete_table(u'importSQLAuthor')

        # Deleting model 'ImportTrainee'
        db.delete_table(u'import_trainee')

        # Deleting model 'Inspectionscore'
        db.delete_table(u'inspectionScore')

        # Deleting model 'Interimcalendar'
        db.delete_table(u'interimCalendar')

        # Deleting model 'Interimexit'
        db.delete_table(u'interimExit')

        # Deleting model 'Interimintention'
        db.delete_table(u'interimIntention')

        # Deleting model 'Leaveslip'
        db.delete_table(u'leaveSlip')

        # Deleting model 'Leaveslipapproval'
        db.delete_table(u'leaveSlipApproval')

        # Deleting model 'Leaveslipcategory'
        db.delete_table(u'leaveSlipCategory')

        # Deleting model 'Leaveslipevent'
        db.delete_table(u'leaveSlipEvent')

        # Deleting model 'Leaveslipmealout'
        db.delete_table(u'leaveSlipMealOut')

        # Deleting model 'Leaveslipmember'
        db.delete_table(u'leaveSlipMember')

        # Deleting model 'Leaveslipnightout'
        db.delete_table(u'leaveSlipNightOut')

        # Deleting model 'Leaveslipstatus'
        db.delete_table(u'leaveSlipStatus')

        # Deleting model 'Leaveslipta'
        db.delete_table(u'leaveSlipTA')

        # Deleting model 'Leavesliptype'
        db.delete_table(u'leaveSlipType')

        # Deleting model 'Leaveslipgroupview'
        db.delete_table(u'leaveslipgroupview')

        # Deleting model 'LeaveslipinfoGroup'
        db.delete_table(u'leaveslipinfo_group')

        # Deleting model 'Leaveslippersonalview'
        db.delete_table(u'leaveslippersonalview')

        # Deleting model 'LinensRequests'
        db.delete_table(u'linens_requests')

        # Deleting model 'LinensTypes'
        db.delete_table(u'linens_types')

        # Deleting model 'Locality'
        db.delete_table(u'locality')

        # Deleting model 'Logbrowser'
        db.delete_table(u'logBrowser')

        # Deleting model 'Logclasslogin'
        db.delete_table(u'logClassLogin')

        # Deleting model 'Loglogin'
        db.delete_table(u'logLogin')

        # Deleting model 'Lognightlytasks'
        db.delete_table(u'logNightlyTasks')

        # Deleting model 'Logpage'
        db.delete_table(u'logPage')

        # Deleting model 'Lookup'
        db.delete_table(u'lookup')

        # Deleting model 'Lsbook'
        db.delete_table(u'lsBook')

        # Deleting model 'Lsoffense'
        db.delete_table(u'lsOffense')

        # Deleting model 'Lsoffensereason'
        db.delete_table(u'lsOffenseReason')

        # Deleting model 'Lssubmission'
        db.delete_table(u'lsSubmission')

        # Deleting model 'MaintenanceRequests'
        db.delete_table(u'maintenance_requests')

        # Deleting model 'MaintenanceTypes'
        db.delete_table(u'maintenance_types')

        # Deleting model 'Mealseatlocation'
        db.delete_table(u'mealSeatLocation')

        # Deleting model 'Mealseating'
        db.delete_table(u'mealSeating')

        # Deleting model 'Newapplications'
        db.delete_table(u'newApplications')

        # Deleting model 'Newapplicationsstatus'
        db.delete_table(u'newApplicationsStatus')

        # Deleting model 'Notesexception'
        db.delete_table(u'notesException')

        # Deleting model 'Notesreceived'
        db.delete_table(u'notesReceived')

        # Deleting model 'Page'
        db.delete_table(u'page')

        # Deleting model 'Pageaccounttype'
        db.delete_table(u'pageAccountType')

        # Deleting model 'Period'
        db.delete_table(u'period')

        # Deleting model 'QuestionEssays'
        db.delete_table(u'question_essays')

        # Deleting model 'QuestionPrompts'
        db.delete_table(u'question_prompts')

        # Deleting model 'Recentupdates'
        db.delete_table(u'recentUpdates')

        # Deleting model 'Recoveryweekday'
        db.delete_table(u'recoveryWeekDay')

        # Deleting model 'Reportcolumn'
        db.delete_table(u'reportColumn')

        # Deleting model 'Reportcolumnquery'
        db.delete_table(u'reportColumnQuery')

        # Deleting model 'Reportquery'
        db.delete_table(u'reportQuery')

        # Deleting model 'Requestcomment'
        db.delete_table(u'requestComment')

        # Deleting model 'Requesttracking'
        db.delete_table(u'requestTracking')

        # Deleting model 'Residence'
        db.delete_table(u'residence')

        # Deleting model 'Residencetype'
        db.delete_table(u'residenceType')

        # Deleting model 'ResidenceRepairs'
        db.delete_table(u'residence_repairs')

        # Deleting model 'ResidenceRoomSections'
        db.delete_table(u'residence_room_sections')

        # Deleting model 'ResidenceRooms'
        db.delete_table(u'residence_rooms')

        # Deleting model 'Rolldata'
        db.delete_table(u'rollData')

        # Deleting model 'Rollevent'
        db.delete_table(u'rollEvent')

        # Deleting model 'Rollstatus'
        db.delete_table(u'rollStatus')

        # Deleting model 'Rollhousefinalization'
        db.delete_table(u'rollhousefinalization')

        # Deleting model 'Rollsubmissiondata'
        db.delete_table(u'rollsubmissiondata')

        # Deleting model 'Rollteamfinalization'
        db.delete_table(u'rollteamfinalization')

        # Deleting model 'Rollypcfinalization'
        db.delete_table(u'rollypcfinalization')

        # Deleting model 'Room'
        db.delete_table(u'room')

        # Deleting model 'Roomlist'
        db.delete_table(u'roomlist')

        # Deleting model 'Roomreservationrequests'
        db.delete_table(u'roomreservationrequests')

        # Deleting model 'Roomschedule'
        db.delete_table(u'roomschedule')

        # Deleting model 'RsMinistrybooks'
        db.delete_table(u'rs_ministryBooks')

        # Deleting model 'RsSyllabus'
        db.delete_table(u'rs_syllabus')

        # Deleting model 'RsSyllabusreadings'
        db.delete_table(u'rs_syllabusReadings')

        # Deleting model 'Savedreport'
        db.delete_table(u'savedReport')

        # Deleting model 'Savedreportcolumn'
        db.delete_table(u'savedReportColumn')

        # Deleting model 'Schedule'
        db.delete_table(u'schedule')

        # Deleting model 'Schedulecategory'
        db.delete_table(u'scheduleCategory')

        # Deleting model 'Scheduleevent'
        db.delete_table(u'scheduleEvent')

        # Deleting model 'Scheduletraineefilter'
        db.delete_table(u'scheduleTraineeFilter')

        # Deleting model 'Seat'
        db.delete_table(u'seat')

        # Deleting model 'Seating'
        db.delete_table(u'seating')

        # Deleting model 'Seatingchart'
        db.delete_table(u'seatingChart')

        # Deleting model 'Seatingevent'
        db.delete_table(u'seatingEvent')

        # Deleting model 'Semiannualstudyattendance'
        db.delete_table(u'semiAnnualStudyAttendance')

        # Deleting model 'Semiannualstudylocation'
        db.delete_table(u'semiAnnualStudyLocation')

        # Deleting model 'Semiannualtesting'
        db.delete_table(u'semiAnnualTesting')

        # Deleting model 'Semiannualtestingrooms'
        db.delete_table(u'semiAnnualTestingRooms')

        # Deleting model 'Sendinglocality'
        db.delete_table(u'sendingLocality')

        # Deleting model 'Svassignment'
        db.delete_table(u'svAssignment')

        # Deleting model 'Svassignmentsave'
        db.delete_table(u'svAssignmentSave')

        # Deleting model 'Svexception'
        db.delete_table(u'svException')

        # Deleting model 'Svexceptionservice'
        db.delete_table(u'svExceptionService')

        # Deleting model 'Svexceptiontrainee'
        db.delete_table(u'svExceptionTrainee')

        # Deleting model 'Svmissedservice'
        db.delete_table(u'svMissedService')

        # Deleting model 'Svnote'
        db.delete_table(u'svNote')

        # Deleting model 'Svpermanentassignment'
        db.delete_table(u'svPermanentAssignment')

        # Deleting model 'Svqualificationgroup'
        db.delete_table(u'svQualificationGroup')

        # Deleting model 'Svreport'
        db.delete_table(u'svReport')

        # Deleting model 'Svreportnote'
        db.delete_table(u'svReportNote')

        # Deleting model 'Svreportservice'
        db.delete_table(u'svReportService')

        # Deleting model 'Svreporttraineecomment'
        db.delete_table(u'svReportTraineeComment')

        # Deleting model 'Svrolldata'
        db.delete_table(u'svRollData')

        # Deleting model 'Svrollevent'
        db.delete_table(u'svRollEvent')

        # Deleting model 'Svscheduleinstance'
        db.delete_table(u'svScheduleInstance')

        # Deleting model 'Svservice'
        db.delete_table(u'svService')

        # Deleting model 'Svservicealgorithm'
        db.delete_table(u'svServiceAlgorithm')

        # Deleting model 'Svservicecategory'
        db.delete_table(u'svServiceCategory')

        # Deleting model 'Svserviceschedule'
        db.delete_table(u'svServiceSchedule')

        # Deleting model 'Svservicesorttype'
        db.delete_table(u'svServiceSortType')

        # Deleting model 'Svservicetime'
        db.delete_table(u'svServiceTime')

        # Deleting model 'Svservicetimescheduleevent'
        db.delete_table(u'svServiceTimeScheduleEvent')

        # Deleting model 'Svservicetoschedulemap'
        db.delete_table(u'svServiceToScheduleMap')

        # Deleting model 'Svservicetraineefilter'
        db.delete_table(u'svServiceTraineeFilter')

        # Deleting model 'Svserviceweeklyreport'
        db.delete_table(u'svServiceWeeklyReport')

        # Deleting model 'Svserviceweeklyreportentry'
        db.delete_table(u'svServiceWeeklyReportEntry')

        # Deleting model 'Svserviceworkergroup'
        db.delete_table(u'svServiceWorkerGroup')

        # Deleting model 'Svserviceworkergroupsnapshot'
        db.delete_table(u'svServiceWorkerGroupSnapshot')

        # Deleting model 'Svserviceworkergrouptraineefilter'
        db.delete_table(u'svServiceWorkerGroupTraineeFilter')

        # Deleting model 'Svworkerexception'
        db.delete_table(u'svWorkerException')

        # Deleting model 'Svworkerqualification'
        db.delete_table(u'svWorkerQualification')

        # Deleting model 'Svworkloadhistory'
        db.delete_table(u'svWorkloadHistory')

        # Deleting model 'Svserviceview'
        db.delete_table(u'svserviceview')

        # Deleting model 'Team'
        db.delete_table(u'team')

        # Deleting model 'Teamschedule'
        db.delete_table(u'teamSchedule')

        # Deleting model 'Teamtype'
        db.delete_table(u'teamType')

        # Deleting model 'Term'
        db.delete_table(u'term')

        # Deleting model 'Tmplsimportoffense'
        db.delete_table(u'tmpLsImportOffense')

        # Deleting model 'Trainee'
        db.delete_table(u'trainee')

        # Deleting model 'Traineefilter'
        db.delete_table(u'traineeFilter')

        # Deleting model 'Traineeschedule'
        db.delete_table(u'traineeSchedule')

        # Deleting model 'Traineestatus'
        db.delete_table(u'traineeStatus')

        # Deleting model 'TraineeOld'
        db.delete_table(u'trainee_old')

        # Deleting model 'Traineeview'
        db.delete_table(u'traineeview')

        # Deleting model 'Trainingassistant'
        db.delete_table(u'trainingAssistant')

        # Deleting model 'Trainingclasses'
        db.delete_table(u'trainingClasses')

        # Deleting model 'Trainingassistantview'
        db.delete_table(u'trainingassistantview')

        # Deleting model 'User'
        db.delete_table(u'user')

        # Deleting model 'Useraccounttype'
        db.delete_table(u'userAccountType')

        # Deleting model 'Waapprovalstatus'
        db.delete_table(u'waApprovalStatus')

        # Deleting model 'Wamaclist'
        db.delete_table(u'waMACList')

        # Deleting model 'Wareason'
        db.delete_table(u'waReason')

        # Deleting model 'Warequest'
        db.delete_table(u'waRequest')

        # Deleting model 'Weatherlocation'
        db.delete_table(u'weatherLocation')

        # Deleting model 'Weekday'
        db.delete_table(u'weekDay')


    models = {
        u'migrate.accounttype': {
            'Meta': {'object_name': 'Accounttype', 'db_table': "u'accountType'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3L'}),
            'databasetable': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'databaseTable'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255L'})
        },
        u'migrate.announcementmember': {
            'Meta': {'object_name': 'Announcementmember', 'db_table': "u'announcementMember'"},
            'announcementrequestid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'announcementRequestID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"}),
            'viewed': ('django.db.models.fields.CharField', [], {'max_length': '3L'})
        },
        u'migrate.announcementrequest': {
            'Meta': {'object_name': 'Announcementrequest', 'db_table': "u'announcementRequest'"},
            'announcement': ('django.db.models.fields.TextField', [], {}),
            'announcementstatusid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'announcementStatusID'"}),
            'announcementtypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'announcementTypeID'"}),
            'date2announce': ('django.db.models.fields.DateField', [], {'db_column': "u'date2Announce'"}),
            'date2hide': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'date2Hide'", 'blank': 'True'}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'dateCreated'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'purpose': ('django.db.models.fields.TextField', [], {}),
            'showcommons': ('django.db.models.fields.IntegerField', [], {'db_column': "u'showCommons'"}),
            'showpaper': ('django.db.models.fields.IntegerField', [], {'db_column': "u'showPaper'"}),
            'showserver': ('django.db.models.fields.IntegerField', [], {'db_column': "u'showServer'"}),
            'ta_userid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ta_userID'", 'blank': 'True'}),
            'tacomments': ('django.db.models.fields.TextField', [], {'db_column': "u'TAComments'", 'blank': 'True'}),
            'typevalue': ('django.db.models.fields.TextField', [], {'db_column': "u'typeValue'", 'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.announcementselection': {
            'Meta': {'object_name': 'Announcementselection', 'db_table': "u'announcementSelection'"},
            'announcementrequestid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'announcementRequestID'"}),
            'foreignid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'foreignID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'migrate.announcementstatus': {
            'Meta': {'object_name': 'Announcementstatus', 'db_table': "u'announcementStatus'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.announcementtype': {
            'Meta': {'object_name': 'Announcementtype', 'db_table': "u'announcementType'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.atrabsenttrainee': {
            'Meta': {'object_name': 'Atrabsenttrainee', 'db_table': "u'atrAbsentTrainee'"},
            'atrrosterid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'atrRosterID'"}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'numdays': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDays'", 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '17L'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.atrroster': {
            'Meta': {'object_name': 'Atrroster', 'db_table': "u'atrRoster'"},
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'})
        },
        u'migrate.atrunreportedhouse': {
            'Meta': {'object_name': 'Atrunreportedhouse', 'db_table': "u'atrUnreportedHouse'"},
            'atrrosterid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'atrRosterID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'residenceID'"})
        },
        u'migrate.attendancesystem': {
            'Meta': {'object_name': 'Attendancesystem', 'db_table': "u'attendancesystem'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3L'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100L'}),
            'term1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'term2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'term3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'term4': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'migrate.attendancetables': {
            'Meta': {'object_name': 'Attendancetables', 'db_table': "u'attendancetables'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'tablename': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'tableName'"})
        },
        u'migrate.avapprovalstatus': {
            'Meta': {'object_name': 'Avapprovalstatus', 'db_table': "u'avApprovalStatus'"},
            'approvalstatus': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'approvalStatus'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"})
        },
        u'migrate.avclass': {
            'Meta': {'object_name': 'Avclass', 'db_table': "u'avClass'"},
            'classyear': ('django.db.models.fields.IntegerField', [], {'db_column': "u'classYear'"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'dayofweek': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'dayOfWeek'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'scheduleeventname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'db_column': "u'scheduleEventName'"})
        },
        u'migrate.avreason': {
            'Meta': {'object_name': 'Avreason', 'db_table': "u'avReason'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.avrequest': {
            'Meta': {'object_name': 'Avrequest', 'db_table': "u'avRequest'"},
            'avapprovalstatusid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'avApprovalStatusID'"}),
            'avclassid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'avClassID'"}),
            'avreasonid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'avReasonID'"}),
            'avrequestcommentid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'avRequestCommentID'", 'blank': 'True'}),
            'classdate': ('django.db.models.fields.DateField', [], {'db_column': "u'classDate'"}),
            'dateapproved': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dateApproved'", 'blank': 'True'}),
            'datesubmitted': ('django.db.models.fields.DateField', [], {'db_column': "u'dateSubmitted'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'tacomments': ('django.db.models.fields.TextField', [], {'db_column': "u'TAComments'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.avrequestcomment': {
            'Meta': {'object_name': 'Avrequestcomment', 'db_table': "u'avRequestComment'"},
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "u'Comments'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'ta_userid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ta_userID'", 'blank': 'True'})
        },
        u'migrate.bostonapp': {
            'Meta': {'object_name': 'Bostonapp', 'db_table': "u'bostonApp'"},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'age': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'application_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'automobile': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'automobile_seats': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bicycle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'citizenship': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'citizenship_other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'college1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'college2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_baptized': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_saved': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'degree1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'degree2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dependents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'english_ability': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_locality': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_locality_date': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'lang_chinese': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_korean': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_spanish': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'major1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'major2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'marital_status': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'marriage_date': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'other_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_cell': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_home': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'previous_training': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'previous_training_graduation_date': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sending_locality': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'service_areas': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouse_age': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouse_attitude': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouse_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouse_occupation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'statement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'submitted': ('django.db.models.fields.IntegerField', [], {}),
            'support_church': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'support_family_friends': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'support_other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'support_yourself': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'trainee_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'migrate.brbooks': {
            'Meta': {'object_name': 'BrBooks', 'db_table': "u'br_books'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30L'})
        },
        u'migrate.brtraineebook': {
            'Meta': {'object_name': 'BrTraineeBook', 'db_table': "u'br_trainee_book'"},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.BrBooks']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Term']"}),
            'trainee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']"})
        },
        u'migrate.bugs': {
            'Meta': {'object_name': 'Bugs', 'db_table': "u'bugs'"},
            'assignedto_userid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'assignedTo_userID'", 'blank': 'True'}),
            'bug': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'datecompleted': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'dateCompleted'"}),
            'datestarted': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'dateStarted'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'isdone': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isDone'"}),
            'isvisible': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'isVisible'"}),
            'pageid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'pageID'"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'projecteddate': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'projectedDate'"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'timeStamp'"}),
            'useragent': ('django.db.models.fields.TextField', [], {'db_column': "u'userAgent'", 'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.bunk': {
            'Meta': {'object_name': 'Bunk', 'db_table': "u'bunk'"},
            'bunkid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'bunkID'", 'blank': 'True'}),
            'bunkno': ('django.db.models.fields.CharField', [], {'max_length': '8L', 'db_column': "u'bunkNo'", 'blank': 'True'}),
            'fttause': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'fttaUse'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roomid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'roomID'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '6L', 'blank': 'True'})
        },
        u'migrate.church': {
            'Meta': {'object_name': 'Church', 'db_table': "u'church'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'migrate.classnotes': {
            'Meta': {'object_name': 'Classnotes', 'db_table': "u'classNotes'"},
            'finalized': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'rolleventid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Rollevent']", 'null': 'True', 'db_column': "u'rollEventID'", 'blank': 'True'}),
            'submissiondate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submissionDate'"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.conference': {
            'Meta': {'object_name': 'Conference', 'db_table': "u'conference'"},
            'allergies': ('django.db.models.fields.TextField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'housing': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.IntegerField', [], {}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.dailybibleverse': {
            'Meta': {'object_name': 'Dailybibleverse', 'db_table': "u'dailyBibleVerse'"},
            'dateadded': ('django.db.models.fields.DateField', [], {'db_column': "u'dateAdded'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'isdisplayed': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isDisplayed'"}),
            'lastdisplayed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'lastDisplayed'", 'blank': 'True'}),
            'verse': ('django.db.models.fields.TextField', [], {}),
            'verseref': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'db_column': "u'verseRef'"})
        },
        u'migrate.dberror': {
            'Meta': {'object_name': 'Dberror', 'db_table': "u'dbError'"},
            'bugsid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'bugsID'"}),
            'error': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'line': ('django.db.models.fields.IntegerField', [], {}),
            'logpageid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'logPageID'", 'blank': 'True'}),
            'query': ('django.db.models.fields.TextField', [], {}),
            'stacktrace': ('django.db.models.fields.TextField', [], {'db_column': "u'stackTrace'"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'migrate.exams': {
            'Meta': {'object_name': 'Exams', 'db_table': "u'exams'"},
            'endtime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'endTime'"}),
            'exam': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'startTime'"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8L'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'trainingclassesid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'trainingClassesID'"}),
            'type': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'migrate.examstraineeaccess': {
            'Meta': {'object_name': 'Examstraineeaccess', 'db_table': "u'examsTraineeAccess'"},
            'examid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'examID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.examstraineeanswers': {
            'Meta': {'object_name': 'Examstraineeanswers', 'db_table': "u'examsTraineeAnswers'"},
            'answers': ('django.db.models.fields.TextField', [], {}),
            'examid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'examID'"}),
            'finalized': ('django.db.models.fields.IntegerField', [], {}),
            'grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lastupdated': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'lastUpdated'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.examstraineeanswersgrades': {
            'Meta': {'object_name': 'Examstraineeanswersgrades', 'db_table': "u'examsTraineeAnswersGrades'"},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '300L', 'blank': 'True'}),
            'examstraineeanswersid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'examsTraineeAnswersID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'questionnumber': ('django.db.models.fields.IntegerField', [], {'db_column': "u'questionNumber'"})
        },
        u'migrate.framerequests': {
            'Meta': {'object_name': 'FrameRequests', 'db_table': "u'frame_requests'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'broken_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'completed': ('django.db.models.fields.IntegerField', [], {}),
            'completed_date': ('django.db.models.fields.DateField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'exists_already': ('django.db.models.fields.IntegerField', [], {}),
            'fix': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'frame_quote': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'residence_id': ('django.db.models.fields.IntegerField', [], {}),
            'trainee_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.globalsettings': {
            'Meta': {'object_name': 'Globalsettings', 'db_table': "u'globalSettings'"},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'migrate.gospelcitizenship': {
            'Meta': {'object_name': 'Gospelcitizenship', 'db_table': "u'gospelCitizenship'"},
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"})
        },
        u'migrate.gospelsurvey': {
            'Meta': {'object_name': 'Gospelsurvey', 'db_table': "u'gospelSurvey'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'options': ('django.db.models.fields.CharField', [], {'max_length': '40L'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'term': ('django.db.models.fields.IntegerField', [], {}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '40L'})
        },
        u'migrate.gospeltripapplication': {
            'Meta': {'object_name': 'Gospeltripapplication', 'db_table': "u'gospelTripApplication'"},
            'car1': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car2': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car3': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car4': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car5': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car6': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'lang1': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'lang2': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'lang3': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'lang4': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'lang5': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'lang6': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'langtext1': ('django.db.models.fields.TextField', [], {'db_column': "u'langText1'", 'blank': 'True'}),
            'langtext2': ('django.db.models.fields.TextField', [], {'db_column': "u'langText2'", 'blank': 'True'}),
            'langtext3': ('django.db.models.fields.TextField', [], {'db_column': "u'langText3'", 'blank': 'True'}),
            'langtext4': ('django.db.models.fields.TextField', [], {'db_column': "u'langText4'", 'blank': 'True'}),
            'langtext5': ('django.db.models.fields.TextField', [], {'db_column': "u'langText5'", 'blank': 'True'}),
            'langtext6': ('django.db.models.fields.TextField', [], {'db_column': "u'langText6'", 'blank': 'True'}),
            'pref1': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'pref2': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'pref3': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'pref4': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'pref5': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'pref6': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'preftext1': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText1'", 'blank': 'True'}),
            'preftext2': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText2'", 'blank': 'True'}),
            'preftext3': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText3'", 'blank': 'True'}),
            'preftext4': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText4'", 'blank': 'True'}),
            'preftext5': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText5'", 'blank': 'True'}),
            'preftext6': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText6'", 'blank': 'True'}),
            'prof1': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'prof2': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'prof3': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'prof4': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'prof5': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'prof6': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'show': ('django.db.models.fields.IntegerField', [], {}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gospeltriparrangement': {
            'Meta': {'object_name': 'Gospeltriparrangement', 'db_table': "u'gospelTripArrangement'"},
            'gospeltriprunid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Gospeltriprun']", 'db_column': "u'gospelTripRunID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.gospeltripassignment': {
            'Meta': {'object_name': 'Gospeltripassignment', 'db_table': "u'gospelTripAssignment'"},
            'balance': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'balancepaid': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'balancePaid'", 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '7L', 'blank': 'True'}),
            'datepaid': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'datePaid'", 'blank': 'True'}),
            'deposit': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'generalcomment': ('django.db.models.fields.TextField', [], {'db_column': "u'generalComment'", 'blank': 'True'}),
            'gospeltripdestinationid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'gospelTripDestinationID'", 'blank': 'True'}),
            'paymentmethod': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'paymentMethod'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gospeltripdestination': {
            'Meta': {'object_name': 'Gospeltripdestination', 'db_table': "u'gospelTripDestination'"},
            'gospeltypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'gospelTypeID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'secondyear': ('django.db.models.fields.IntegerField', [], {'db_column': "u'secondYear'"})
        },
        u'migrate.gospeltripdriver': {
            'Meta': {'object_name': 'Gospeltripdriver', 'db_table': "u'gospelTripDriver'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'})
        },
        u'migrate.gospeltripflight': {
            'Meta': {'object_name': 'Gospeltripflight', 'db_table': "u'gospelTripFlight'"},
            'flightcomment': ('django.db.models.fields.TextField', [], {'db_column': "u'flightComment'", 'blank': 'True'}),
            'interoutairline': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interOutAirline'", 'blank': 'True'}),
            'interoutarrivalairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interOutArrivalAirport'", 'blank': 'True'}),
            'interoutarrivaldatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'interOutArrivalDateTime'", 'blank': 'True'}),
            'interoutdeptairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interOutDeptAirport'", 'blank': 'True'}),
            'interoutdeptdatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'interOutDeptDateTime'", 'blank': 'True'}),
            'interoutflightnumber': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interOutFlightNumber'", 'blank': 'True'}),
            'interretairline': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interRetAirline'", 'blank': 'True'}),
            'interretarrivalairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interRetArrivalAirport'", 'blank': 'True'}),
            'interretarrivaldatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'interRetArrivalDateTime'", 'blank': 'True'}),
            'interretdeptairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interRetDeptAirport'", 'blank': 'True'}),
            'interretdeptdatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'interRetDeptDateTime'", 'blank': 'True'}),
            'interretflightnumber': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'interRetFlightNumber'", 'blank': 'True'}),
            'outairline': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'outAirline'", 'blank': 'True'}),
            'outarrivalairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'outArrivalAirport'", 'blank': 'True'}),
            'outarrivaldatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'outArrivalDateTime'", 'blank': 'True'}),
            'outdeptairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'outDeptAirport'", 'blank': 'True'}),
            'outdeptdatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'outDeptDateTime'", 'blank': 'True'}),
            'outflightnumber': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'outFlightNumber'", 'blank': 'True'}),
            'retairline': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'retAirline'", 'blank': 'True'}),
            'retarrivalairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'retArrivalAirport'", 'blank': 'True'}),
            'retarrivaldatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'retArrivalDateTime'", 'blank': 'True'}),
            'retdeptairport': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'retDeptAirport'", 'blank': 'True'}),
            'retdeptdatetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'retDeptDateTime'", 'blank': 'True'}),
            'retflightnumber': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'retFlightNumber'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gospeltripinformation': {
            'Meta': {'object_name': 'Gospeltripinformation', 'db_table': "u'gospelTripInformation'"},
            'allergy': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'costavailable': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'db_column': "u'costAvailable'", 'blank': 'True'}),
            'costcovered': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'costCovered'"}),
            'departingairport': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'db_column': "u'departingAirport'", 'blank': 'True'}),
            'flightcovered': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'flightCovered'"}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'gospelcitizenshipid': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'gospelCitizenshipID'"}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'mname': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"}),
            'vehicle': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'vehicleavailable': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'vehicleAvailable'"}),
            'vehicleinsurance': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'db_column': "u'vehicleInsurance'", 'blank': 'True'})
        },
        u'migrate.gospeltriplanguage': {
            'Meta': {'object_name': 'Gospeltriplanguage', 'db_table': "u'gospelTripLanguage'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.gospeltripoverseer': {
            'Meta': {'object_name': 'Gospeltripoverseer', 'db_table': "u'gospelTripOverseer'"},
            'car1': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car2': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car3': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car4': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car5': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'car6': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'contact': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'db_column': "u'firstName'", 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'lang1': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'lang2': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'lang3': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'lang4': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'lang5': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'lang6': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'langtext1': ('django.db.models.fields.TextField', [], {'db_column': "u'langText1'", 'blank': 'True'}),
            'langtext2': ('django.db.models.fields.TextField', [], {'db_column': "u'langText2'", 'blank': 'True'}),
            'langtext3': ('django.db.models.fields.TextField', [], {'db_column': "u'langText3'", 'blank': 'True'}),
            'langtext4': ('django.db.models.fields.TextField', [], {'db_column': "u'langText4'", 'blank': 'True'}),
            'langtext5': ('django.db.models.fields.TextField', [], {'db_column': "u'langText5'", 'blank': 'True'}),
            'langtext6': ('django.db.models.fields.TextField', [], {'db_column': "u'langText6'", 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'db_column': "u'lastName'", 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'pref1': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'pref2': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'pref3': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'pref4': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'pref5': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'pref6': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'preftext1': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText1'", 'blank': 'True'}),
            'preftext2': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText2'", 'blank': 'True'}),
            'preftext3': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText3'", 'blank': 'True'}),
            'preftext4': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText4'", 'blank': 'True'}),
            'preftext5': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText5'", 'blank': 'True'}),
            'preftext6': ('django.db.models.fields.TextField', [], {'db_column': "u'prefText6'", 'blank': 'True'}),
            'prof1': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'prof2': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'prof3': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'prof4': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'prof5': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'prof6': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gospeltrippassport': {
            'Meta': {'object_name': 'Gospeltrippassport', 'db_table': "u'gospelTripPassport'"},
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'expirationdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'expirationDate'", 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'gospelcitizenshipid': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'gospelCitizenshipID'"}),
            'gospelcitizenshipother': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'gospelCitizenshipOther'", 'blank': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'mname': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'passportnumber': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'passportNumber'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gospeltrippayment': {
            'Meta': {'object_name': 'Gospeltrippayment', 'db_table': "u'gospelTripPayment'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.gospeltripproficiency': {
            'Meta': {'object_name': 'Gospeltripproficiency', 'db_table': "u'gospelTripProficiency'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proficiency': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.gospeltriprun': {
            'Meta': {'object_name': 'Gospeltriprun', 'db_table': "u'gospelTripRun'"},
            'endloc': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'db_column': "u'endLoc'", 'blank': 'True'}),
            'gospeltripvehicleid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Gospeltripvehicle']", 'null': 'True', 'db_column': "u'gospelTripVehicleID'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200L'}),
            'startloc': ('django.db.models.fields.CharField', [], {'max_length': '200L', 'db_column': "u'startLoc'", 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'migrate.gospeltriprundriver': {
            'Meta': {'object_name': 'Gospeltriprundriver', 'db_table': "u'gospelTripRunDriver'"},
            'gospeltripdriverid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Gospeltripdriver']", 'db_column': "u'gospelTripDriverID'"}),
            'gospeltriprunid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Gospeltriprun']", 'db_column': "u'gospelTripRunID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'migrate.gospeltripselection': {
            'Meta': {'object_name': 'Gospeltripselection', 'db_table': "u'gospelTripSelection'"},
            'gospeltypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'gospelTypeID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gospeltripvehicle': {
            'Meta': {'object_name': 'Gospeltripvehicle', 'db_table': "u'gospelTripVehicle'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'numpassenger': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numPassenger'", 'blank': 'True'}),
            'vehiclename': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'vehicleName'"})
        },
        u'migrate.gospeltype': {
            'Meta': {'object_name': 'Gospeltype', 'db_table': "u'gospelType'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.gp': {
            'Meta': {'object_name': 'Gp', 'db_table': "u'gp'"},
            'active': ('django.db.models.fields.IntegerField', [], {'db_column': "u'Active'"}),
            'gpid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'gpID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'termname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'db_column': "u'termName'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.gpstats': {
            'Meta': {'object_name': 'Gpstats', 'db_table': "u'gpStats'"},
            'gpid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'gpID'"}),
            'gptypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'gpTypeID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'teamid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'teamID'"}),
            'termname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'db_column': "u'termName'"}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'week': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.gpteam': {
            'Meta': {'object_name': 'Gpteam', 'db_table': "u'gpTeam'"},
            'gpid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'gpID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'teamid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'teamID'"})
        },
        u'migrate.gptype': {
            'Meta': {'object_name': 'Gptype', 'db_table': "u'gpType'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'statname': ('django.db.models.fields.CharField', [], {'max_length': '26L', 'db_column': "u'statName'"})
        },
        u'migrate.gradactivity': {
            'Meta': {'object_name': 'GradActivity', 'db_table': "u'grad_activity'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32L'})
        },
        u'migrate.gradadmin': {
            'Meta': {'object_name': 'GradAdmin', 'db_table': "u'grad_admin'"},
            'duedate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dueDate'", 'blank': 'True'}),
            'gradactivityid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'gradActivityID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'showactivity': ('django.db.models.fields.IntegerField', [], {'db_column': "u'showActivity'"})
        },
        u'migrate.gradconsiderations': {
            'Meta': {'object_name': 'GradConsiderations', 'db_table': "u'grad_considerations'"},
            'attend': ('django.db.models.fields.CharField', [], {'max_length': '4L', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fellowship': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'finance': ('django.db.models.fields.CharField', [], {'max_length': '4L', 'blank': 'True'}),
            'plans': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gradinvites': {
            'Meta': {'object_name': 'GradInvites', 'db_table': "u'grad_invites'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'num_dvd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_invites': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.gradremembrance': {
            'Meta': {'object_name': 'GradRemembrance', 'db_table': "u'grad_remembrance'"},
            'localityid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'localityID'", 'blank': 'True'}),
            'reference': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'remembrance1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'remembrance2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'traineeID'"})
        },
        u'migrate.gradspeaking': {
            'Meta': {'object_name': 'GradSpeaking', 'db_table': "u'grad_speaking'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaking': ('django.db.models.fields.TextField', [], {}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.gradstats': {
            'Meta': {'object_name': 'GradStats', 'db_table': "u'grad_stats'"},
            'burden1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'burden2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'burden3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'num_invites': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'plans': ('django.db.models.fields.TextField', [], {}),
            'pref1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pref2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pref3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'q1': ('django.db.models.fields.IntegerField', [], {}),
            'q2': ('django.db.models.fields.TextField', [], {}),
            'q3': ('django.db.models.fields.TextField', [], {}),
            'q4': ('django.db.models.fields.IntegerField', [], {}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.gradsurvey': {
            'Meta': {'object_name': 'GradSurvey', 'db_table': "u'grad_survey'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'outline': ('django.db.models.fields.TextField', [], {}),
            'outlinesections': ('django.db.models.fields.IntegerField', [], {'db_column': "u'outlineSections'"}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"})
        },
        u'migrate.gradtestimony': {
            'Meta': {'object_name': 'GradTestimony', 'db_table': "u'grad_testimony'"},
            'fellowship': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fellowship_speak': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'question4': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'termID'", 'blank': 'True'}),
            'testimony': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'testimony_speak': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'traineeID'", 'blank': 'True'})
        },
        u'migrate.greekparsing': {
            'Meta': {'object_name': 'Greekparsing', 'db_table': "u'greekParsing'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'migrate.greekuserstats': {
            'Meta': {'object_name': 'Greekuserstats', 'db_table': "u'greekUserStats'"},
            'correct': ('django.db.models.fields.IntegerField', [], {}),
            'greekvocabid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'greekVocabID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'numtimes': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numTimes'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.greekvocab': {
            'Meta': {'object_name': 'Greekvocab', 'db_table': "u'greekVocab'"},
            'chapter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'english': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'greek': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'parsingid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'parsingID'", 'blank': 'True'})
        },
        u'migrate.gtcasurvey': {
            'Meta': {'object_name': 'Gtcasurvey', 'db_table': "u'gtcaSurvey'"},
            'capacity': ('django.db.models.fields.TextField', [], {}),
            'charlottesville': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'college': ('django.db.models.fields.TextField', [], {}),
            'fellowship': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'fortcollins': ('django.db.models.fields.CharField', [], {'max_length': '5L', 'db_column': "u'fortCollins'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'joinmonth': ('django.db.models.fields.IntegerField', [], {'db_column': "u'joinMonth'"}),
            'joinyear': ('django.db.models.fields.IntegerField', [], {'db_column': "u'joinYear'"}),
            'length': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'locality': ('django.db.models.fields.TextField', [], {}),
            'madison': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'major': ('django.db.models.fields.TextField', [], {}),
            'montreal': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'philadelphia': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'released': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'term': ('django.db.models.fields.IntegerField', [], {}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.hcrecmd': {
            'Meta': {'object_name': 'Hcrecmd', 'db_table': "u'HCRecmd'"},
            'choice': ('django.db.models.fields.IntegerField', [], {}),
            'evalcriterion1': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion1'"}),
            'evalcriterion2': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion2'"}),
            'evalcriterion3': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion3'"}),
            'evalcriterion4': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion4'"}),
            'evalcriterion5': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion5'"}),
            'evalcriterion6': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion6'"}),
            'evalcriterion7': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion7'"}),
            'evalcriterion8': ('django.db.models.fields.IntegerField', [], {'db_column': "u'evalCriterion8'"}),
            'hcuserid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'HCUserID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'db_column': "u'Notes'", 'blank': 'True'}),
            'recmdhcuserid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'recmdHCUserID'"}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ResidenceID'"}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"})
        },
        u'migrate.hcrecmdcriteria': {
            'Meta': {'object_name': 'Hcrecmdcriteria', 'db_table': "u'HCRecmdCriteria'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'max': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'min': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'})
        },
        u'migrate.hcrecmdqs': {
            'Meta': {'object_name': 'Hcrecmdqs', 'db_table': "u'hcrecmdqs'"},
            'atmosphere': ('django.db.models.fields.TextField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'hcuserid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'HCUserID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ResidenceID'"}),
            'situations': ('django.db.models.fields.TextField', [], {}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"})
        },
        u'migrate.hcsurvey': {
            'Meta': {'object_name': 'Hcsurvey', 'db_table': "u'hcSurvey'"},
            'atmosphere': ('django.db.models.fields.TextField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'hcuserid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'HCUserID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'periodid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'periodID'", 'blank': 'True'}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ResidenceID'"}),
            'situations': ('django.db.models.fields.TextField', [], {})
        },
        u'migrate.hcsurveytraineenotes': {
            'Meta': {'object_name': 'Hcsurveytraineenotes', 'db_table': "u'hcSurveyTraineeNotes'"},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'hcsurveyid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'hcSurveyID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.houseinspectionfaq': {
            'Meta': {'object_name': 'Houseinspectionfaq', 'db_table': "u'houseInspectionFAQ'"},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'askerid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'askerID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '14L'}),
            'useful': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.importsql': {
            'Meta': {'object_name': 'Importsql', 'db_table': "u'importSQL'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'iscompleted': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isCompleted'"}),
            'sqlstatement': ('django.db.models.fields.TextField', [], {'db_column': "u'sqlStatement'"}),
            'transactionid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'transactionID'"}),
            'undostatement': ('django.db.models.fields.TextField', [], {'db_column': "u'undoStatement'", 'blank': 'True'})
        },
        u'migrate.importsqlauthor': {
            'Meta': {'object_name': 'Importsqlauthor', 'db_table': "u'importSQLAuthor'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'isfinished': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'isFinished'", 'blank': 'True'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'timebegin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'timeBegin'", 'blank': 'True'}),
            'transactionid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'transactionID'"}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.importtrainee': {
            'Meta': {'object_name': 'ImportTrainee', 'db_table': "u'import_trainee'"},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthdate': ('django.db.models.fields.TextField', [], {'db_column': "u'birthDate'", 'blank': 'True'}),
            'cellnumber': ('django.db.models.fields.TextField', [], {'db_column': "u'cellNumber'", 'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'college': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'couple': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'datebegin': ('django.db.models.fields.TextField', [], {'db_column': "u'dateBegin'", 'blank': 'True'}),
            'degree': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergencyaddress': ('django.db.models.fields.TextField', [], {'db_column': "u'emergencyAddress'", 'blank': 'True'}),
            'emergencycontact': ('django.db.models.fields.TextField', [], {'db_column': "u'emergencyContact'", 'blank': 'True'}),
            'emergencyphone': ('django.db.models.fields.TextField', [], {'db_column': "u'emergencyPhone'", 'blank': 'True'}),
            'emergencyphone2': ('django.db.models.fields.TextField', [], {'db_column': "u'emergencyPhone2'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.TextField', [], {'db_column': "u'firstName'", 'blank': 'True'}),
            'gender': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gospelpref1': ('django.db.models.fields.TextField', [], {'db_column': "u'gospelPref1'", 'blank': 'True'}),
            'gospelpref2': ('django.db.models.fields.TextField', [], {'db_column': "u'gospelPref2'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.TextField', [], {'db_column': "u'lastName'", 'blank': 'True'}),
            'maidenname': ('django.db.models.fields.TextField', [], {'db_column': "u'maidenName'", 'blank': 'True'}),
            'major': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'maritalstatus': ('django.db.models.fields.TextField', [], {'db_column': "u'maritalStatus'", 'blank': 'True'}),
            'mentor': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'middleinitial': ('django.db.models.fields.TextField', [], {'db_column': "u'middleInitial'", 'blank': 'True'}),
            'nickname': ('django.db.models.fields.TextField', [], {'db_column': "u'nickName'", 'blank': 'True'}),
            'officeid': ('django.db.models.fields.TextField', [], {'db_column': "u'officeID'", 'blank': 'True'}),
            'phonenumber': ('django.db.models.fields.TextField', [], {'db_column': "u'phoneNumber'", 'blank': 'True'}),
            'readnt': ('django.db.models.fields.TextField', [], {'db_column': "u'readNT'", 'blank': 'True'}),
            'readot': ('django.db.models.fields.TextField', [], {'db_column': "u'readOT'", 'blank': 'True'}),
            'residenceid': ('django.db.models.fields.TextField', [], {'db_column': "u'residenceID'", 'blank': 'True'}),
            'sendinglocality': ('django.db.models.fields.TextField', [], {'db_column': "u'sendingLocality'", 'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stft': ('django.db.models.fields.TextField', [], {'db_column': "u'STFT'", 'blank': 'True'}),
            'stpt': ('django.db.models.fields.TextField', [], {'db_column': "u'STPT'", 'blank': 'True'}),
            'ta': ('django.db.models.fields.TextField', [], {'db_column': "u'TA'", 'blank': 'True'}),
            'teamid': ('django.db.models.fields.TextField', [], {'db_column': "u'teamID'", 'blank': 'True'}),
            'termscompleted': ('django.db.models.fields.TextField', [], {'db_column': "u'termsCompleted'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'traineeID'", 'blank': 'True'}),
            'vehiclecapacity': ('django.db.models.fields.TextField', [], {'db_column': "u'vehicleCapacity'", 'blank': 'True'}),
            'vehiclecolor': ('django.db.models.fields.TextField', [], {'db_column': "u'vehicleColor'", 'blank': 'True'}),
            'vehicleinfo': ('django.db.models.fields.TextField', [], {'db_column': "u'vehicleInfo'", 'blank': 'True'}),
            'vehiclelicense': ('django.db.models.fields.TextField', [], {'db_column': "u'vehicleLicense'", 'blank': 'True'}),
            'zip': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'migrate.inspectionscore': {
            'Meta': {'object_name': 'Inspectionscore', 'db_table': "u'inspectionScore'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'inspectoruserid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'inspectorUserID'", 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'residenceID'"}),
            'ricuserid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'RICUserID'", 'blank': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'uninspectable': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.interimcalendar': {
            'Meta': {'object_name': 'Interimcalendar', 'db_table': "u'interimCalendar'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {'db_column': "u'endDate'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'startdate': ('django.db.models.fields.DateField', [], {'db_column': "u'startDate'"}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.interimexit': {
            'Meta': {'object_name': 'Interimexit', 'db_table': "u'interimExit'"},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interimintentionid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'interimIntentionID'"}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"}),
            'unsure': ('django.db.models.fields.CharField', [], {'max_length': '3L'})
        },
        u'migrate.interimintention': {
            'Meta': {'object_name': 'Interimintention', 'db_table': "u'interimIntention'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'placeholder': ('django.db.models.fields.TextField', [], {'db_column': "u'placeHolder'", 'blank': 'True'})
        },
        u'migrate.leaveslip': {
            'Meta': {'object_name': 'Leaveslip', 'db_table': "u'leaveSlip'"},
            'assignedtaid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'assignedTAID'", 'blank': 'True'}),
            'didnotinform': ('django.db.models.fields.IntegerField', [], {'db_column': "u'didNotInform'"}),
            'haspaperleaveslip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'hasPaperLeaveSlip'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'informeduserid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'informedUserID'", 'blank': 'True'}),
            'leaveslipcategoryid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Leaveslipcategory']", 'db_column': "u'leaveSlipCategoryID'"}),
            'remarks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'requiresfellowship': ('django.db.models.fields.IntegerField', [], {'db_column': "u'requiresFellowship'"}),
            'sistertaapproval': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'sisterTAApproval'", 'blank': 'True'}),
            'submissiondatetime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submissionDateTime'"}),
            'svscheduleinstanceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svscheduleinstance']", 'null': 'True', 'db_column': "u'svScheduleInstanceID'", 'blank': 'True'}),
            'svserviceid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svServiceID'", 'blank': 'True'}),
            'taprivateremarks': ('django.db.models.fields.TextField', [], {'db_column': "u'TAPrivateRemarks'", 'blank': 'True'}),
            'taremarks': ('django.db.models.fields.TextField', [], {'db_column': "u'TARemarks'", 'blank': 'True'}),
            'texted': ('django.db.models.fields.IntegerField', [], {}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'db_column': "u'userID'"})
        },
        u'migrate.leaveslipapproval': {
            'Meta': {'object_name': 'Leaveslipapproval', 'db_table': "u'leaveSlipApproval'"},
            'affectsperfectattendance': ('django.db.models.fields.IntegerField', [], {'db_column': "u'affectsPerfectAttendance'"}),
            'approvaldatetime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'approvalDateTime'"}),
            'approvalstatus': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'approvalStatus'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leaveslipid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Leaveslip']", 'unique': 'True', 'db_column': "u'leaveSlipID'"}),
            'remarks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'db_column': "u'userID'"})
        },
        u'migrate.leaveslipcategory': {
            'Meta': {'object_name': 'Leaveslipcategory', 'db_table': "u'leaveSlipCategory'"},
            'affectsperfectattendance': ('django.db.models.fields.IntegerField', [], {'db_column': "u'affectsPerfectAttendance'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leavesliptypeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Leavesliptype']", 'db_column': "u'leaveSlipTypeID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'special': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.leaveslipevent': {
            'Meta': {'object_name': 'Leaveslipevent', 'db_table': "u'leaveSlipEvent'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leaveslipid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Leaveslip']", 'db_column': "u'leaveSlipID'"}),
            'scheduleeventid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Scheduleevent']", 'db_column': "u'scheduleEventID'"})
        },
        u'migrate.leaveslipgroupview': {
            'Meta': {'object_name': 'Leaveslipgroupview', 'db_table': "u'leaveslipgroupview'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaveslipcategoryid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'leaveSlipCategoryID'"}),
            'leaveslipid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'leaveSlipID'"}),
            'scheduleeventid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'scheduleEventID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.leaveslipinfogroup': {
            'Meta': {'object_name': 'LeaveslipinfoGroup', 'db_table': "u'leaveslipinfo_group'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'endTime'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leaveslipid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'leaveSlipID'"}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'startTime'"})
        },
        u'migrate.leaveslipmealout': {
            'Meta': {'object_name': 'Leaveslipmealout', 'db_table': "u'leaveSlipMealOut'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leaveslipid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'leaveSlipID'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'blank': 'True'})
        },
        u'migrate.leaveslipmember': {
            'Meta': {'object_name': 'Leaveslipmember', 'db_table': "u'leaveSlipMember'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leaveslipid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Leaveslip']", 'db_column': "u'leaveSlipID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.leaveslipnightout': {
            'Meta': {'object_name': 'Leaveslipnightout', 'db_table': "u'leaveSlipNightOut'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'hcname': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'db_column': "u'HCname'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leaveslipid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'leaveSlipID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14L', 'blank': 'True'}),
            'verifyhc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'verifyHC'", 'blank': 'True'})
        },
        u'migrate.leaveslippersonalview': {
            'Meta': {'object_name': 'Leaveslippersonalview', 'db_table': "u'leaveslippersonalview'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaveslipcategoryid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'leaveSlipCategoryID'"}),
            'leaveslipid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'leaveSlipID'"}),
            'scheduleeventid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'scheduleEventID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.leaveslipstatus': {
            'Meta': {'object_name': 'Leaveslipstatus', 'db_table': "u'leaveSlipStatus'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'statuscode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2L', 'db_column': "u'statusCode'"})
        },
        u'migrate.leaveslipta': {
            'Meta': {'object_name': 'Leaveslipta', 'db_table': "u'leaveSlipTA'"},
            'date_assigned': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'leaveslipid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'leaveSlipID'", 'blank': 'True'}),
            'trainingassistantid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'trainingAssistantID'", 'blank': 'True'})
        },
        u'migrate.leavesliptype': {
            'Meta': {'object_name': 'Leavesliptype', 'db_table': "u'leaveSlipType'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'migrate.linensrequests': {
            'Meta': {'object_name': 'LinensRequests', 'db_table': "u'linens_requests'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'completed': ('django.db.models.fields.IntegerField', [], {}),
            'completed_date': ('django.db.models.fields.DateField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'residence_id': ('django.db.models.fields.IntegerField', [], {}),
            'trainee_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.linenstypes': {
            'Meta': {'object_name': 'LinensTypes', 'db_table': "u'linens_types'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.locality': {
            'Meta': {'object_name': 'Locality', 'db_table': "u'locality'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255L', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'mrtype': ('django.db.models.fields.IntegerField', [], {'db_column': "u'MRType'"})
        },
        u'migrate.logbrowser': {
            'Meta': {'object_name': 'Logbrowser', 'db_table': "u'logBrowser'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'migrate.logclasslogin': {
            'Meta': {'object_name': 'Logclasslogin', 'db_table': "u'logClassLogin'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'ipaddress': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'db_column': "u'ipAddress'"}),
            'session': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.loglogin': {
            'Meta': {'object_name': 'Loglogin', 'db_table': "u'logLogin'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'ipaddr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ipAddr'", 'blank': 'True'}),
            'session': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '7L'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '32L'})
        },
        u'migrate.lognightlytasks': {
            'Meta': {'object_name': 'Lognightlytasks', 'db_table': "u'logNightlyTasks'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'messages': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32L'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'migrate.logpage': {
            'Meta': {'object_name': 'Logpage', 'db_table': "u'logPage'"},
            'browserid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'browserID'", 'blank': 'True'}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'endTime'", 'blank': 'True'}),
            'getparam': ('django.db.models.fields.TextField', [], {'db_column': "u'getParam'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'loadtime': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'loadTime'", 'blank': 'True'}),
            'pageid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'pageID'", 'blank': 'True'}),
            'pageurl': ('django.db.models.fields.TextField', [], {'db_column': "u'pageUrl'", 'blank': 'True'}),
            'postparam': ('django.db.models.fields.TextField', [], {'db_column': "u'postParam'", 'blank': 'True'}),
            'session': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'blank': 'True'}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'startTime'"}),
            'userid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'userID'", 'blank': 'True'})
        },
        u'migrate.lookup': {
            'Meta': {'object_name': 'Lookup', 'db_table': "u'lookup'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'migrate.lsbook': {
            'Meta': {'object_name': 'Lsbook', 'db_table': "u'lsBook'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '8L', 'blank': 'True'}),
            'nummessages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numMessages'", 'blank': 'True'})
        },
        u'migrate.lsoffense': {
            'Meta': {'object_name': 'Lsoffense', 'db_table': "u'lsOffense'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'creationdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'creationDate'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'iscurrentlymondayoffense': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isCurrentlyMondayOffense'"}),
            'lastupdatedate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'lastUpdateDate'"}),
            'lsoffensereasonid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'lsOffenseReasonID'"}),
            'manualhandling': ('django.db.models.fields.IntegerField', [], {'db_column': "u'manualHandling'"}),
            'numlsowed': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numLSOwed'"}),
            'numlsreceived': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numLSReceived'"}),
            'numlsunapplied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numLSUnapplied'", 'blank': 'True'}),
            'signedin': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'signedIn'", 'blank': 'True'}),
            'tacomments': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'taComments'", 'blank': 'True'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.lsoffensereason': {
            'Meta': {'object_name': 'Lsoffensereason', 'db_table': "u'lsOffenseReason'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'ismondayoffense': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'isMondayOffense'", 'blank': 'True'}),
            'numls': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numLS'", 'blank': 'True'}),
            'offensereason': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'db_column': "u'offenseReason'"})
        },
        u'migrate.lssubmission': {
            'Meta': {'object_name': 'Lssubmission', 'db_table': "u'lsSubmission'"},
            'approved': ('django.db.models.fields.IntegerField', [], {}),
            'finalized': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lsbookid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'lsBookID'", 'blank': 'True'}),
            'lsoffenseid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'lsOffenseID'", 'blank': 'True'}),
            'messagenumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'messageNumber'", 'blank': 'True'}),
            'submissiondate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submissionDate'"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.maintenancerequests': {
            'Meta': {'object_name': 'MaintenanceRequests', 'db_table': "u'maintenance_requests'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'completed': ('django.db.models.fields.IntegerField', [], {}),
            'completed_date': ('django.db.models.fields.DateField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'other_room': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'residence_id': ('django.db.models.fields.IntegerField', [], {}),
            'room_id': ('django.db.models.fields.IntegerField', [], {}),
            'trainee_id': ('django.db.models.fields.IntegerField', [], {}),
            'type_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.maintenancetypes': {
            'Meta': {'object_name': 'MaintenanceTypes', 'db_table': "u'maintenance_types'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100L'})
        },
        u'migrate.mealseating': {
            'Meta': {'object_name': 'Mealseating', 'db_table': "u'mealSeating'"},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'maxcapacity': ('django.db.models.fields.IntegerField', [], {'db_column': "u'maxCapacity'"}),
            'mealseatlocationid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'mealSeatLocationID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'numberoccupied': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numberOccupied'"})
        },
        u'migrate.mealseatlocation': {
            'Meta': {'object_name': 'Mealseatlocation', 'db_table': "u'mealSeatLocation'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '9L'})
        },
        u'migrate.newapplications': {
            'Meta': {'object_name': 'Newapplications', 'db_table': "u'newApplications'"},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'aka': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'alcohol': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'applicationid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'applicationID'"}),
            'approval': ('django.db.models.fields.CharField', [], {'max_length': '13L', 'blank': 'True'}),
            'attend_explain': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'attend_two_years': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'audio_video': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'auto_mechanics': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'automobile': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'automobile_color': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'automobile_license': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'automobile_model': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'automobile_seats': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bachelors': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'carpentry': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'churchdate': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'citizen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'citizenship': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'college': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'college2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'college2_country': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'college_country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'college_grad_date': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comp_database': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comp_hardware': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comp_networking': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comp_programming': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'consecration': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'blank': 'True'}),
            'country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cxrayresult': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'datebaptized': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dateofmarriage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'datesaved': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'degree': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'degree2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'deleted': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'dependent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'drugs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elder_abide_relationship_restriction': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'elder_eldercell': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elder_elderemail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elder_elderfname': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elder_elderlname': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elder_erec_complete': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'elder_eRec_complete'", 'blank': 'True'}),
            'elder_in_relationship': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'elder_knowledge': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'elder_paper_recommendation': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'elder_participation': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'elder_recommend': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'blank': 'True'}),
            'elder_recommendation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elder_relationship_explain': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elder_shepherd': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'blank': 'True'}),
            'elder_shepherd_cell': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'blank': 'True'}),
            'elder_shepherd_email': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'blank': 'True'}),
            'elder_understand_english': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'elder_understand_possible_dismissal': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'elder_understand_relationship_restriction': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'blank': 'True'}),
            'elder_work_ethic': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'elder_work_together': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'electrical': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergencyaddress': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergencyemail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergencyname': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergencytelephone': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergencytelephone2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exam': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'facility_maint': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'firstcontact': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'floor_covering': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'full_time_date': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gardening': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gospelpref1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gospelpref2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic_design': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'health_concerns': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hepatitisa1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hepatitisa2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hepatitisb1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hepatitisb2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hepatitisb3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'immunizations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'insurance': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'international_comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'internationalforms': ('django.db.models.fields.CharField', [], {'max_length': '84L', 'db_column': "u'internationalForms'", 'blank': 'True'}),
            'landscaping': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_cantonese': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_chinese': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_korean': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_mandarin': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lang_spanish': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'language_or_char': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lname': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'locality': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'locality_country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'locality_other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'locality_other_country': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'locality_state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'maidenname': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'major': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'major2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'maritalstatus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med10': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med11': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med12': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med13': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med14': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med15': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med16': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med17_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med17_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med17_3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med18': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med19': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med20': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med21': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med22': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med23_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med23_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med24': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med25': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med28': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med28_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med2list': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med30': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med3list': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_4': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_5': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_6': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_7': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4_8': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med4list': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med5': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med6': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med6a': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med7': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med8': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_10': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_4': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_5': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_6': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_7': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_8': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med9_9': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'med_comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'medapproval': ('django.db.models.fields.CharField', [], {'max_length': '18L', 'blank': 'True'}),
            'medical_training': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mmr1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mmr2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mname': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'otherlang': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'overseer_comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pertinantinformation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_cell': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_home': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_international_cell': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_international_home': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture_framing': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'plumbing': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'poor_english': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'previoustraining': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'previoustraining2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'previoustrainingdate': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prof_writing': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'raisedinchurch': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'read_nt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'read_ot': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'security_safety': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'serviceareas': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sewing': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skills_other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouse_attending': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouse_plans': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouseage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouseattitude': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spousename': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spouseoccupation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'support_church': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'support_family': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'support_other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'support_other_value': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'support_yourself': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tbdate': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tbresult': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'td_test': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'terms': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'testimony': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'tobacco': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'twitter': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"}),
            'web_programming': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'xray': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'xraydate': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'zip': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'migrate.newapplicationsstatus': {
            'Meta': {'object_name': 'Newapplicationsstatus', 'db_table': "u'newApplicationsStatus'"},
            'approvedandrew': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'approvedAndrew'"}),
            'approveddennis': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'approvedDennis'"}),
            'approvedmedical': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'approvedMedical'"}),
            'approvedoverall': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'approvedOverall'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'newapplicationsid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'newApplicationsID'"}),
            'provisionalacceptance': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'provisionalAcceptance'"}),
            'provisionalmedical': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'provisionalMedical'"}),
            'sentacceptance': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentAcceptance'"}),
            'sentacknowledgement': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentAcknowledgement'"}),
            'sentarrivalinstructions': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentArrivalInstructions'"}),
            'sentattire': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentAttire'"}),
            'sentbiblereading': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentBibleReading'"}),
            'sentbooks': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentBooks'"}),
            'sentbrodenniswelcome': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentBroDennisWelcome'"}),
            'sentfinance': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentFinance'"}),
            'sentinsurance': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentInsurance'"}),
            'sentmedicial': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentMedicial'"}),
            'sentmentor': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentMentor'"}),
            'sentsecurityandsafety': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentSecurityAndSafety'"}),
            'senttawelcome': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentTAWelcome'"}),
            'sentwebsiteinfo': ('django.db.models.fields.CharField', [], {'max_length': '3L', 'db_column': "u'sentWebsiteInfo'"}),
            'timestampsentacknowledgement': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'timestampSentAcknowledgement'"})
        },
        u'migrate.notesexception': {
            'Meta': {'object_name': 'Notesexception', 'db_table': "u'notesException'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'scheduleeventid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Scheduleevent']", 'db_column': "u'scheduleEventID'"})
        },
        u'migrate.notesreceived': {
            'Meta': {'object_name': 'Notesreceived', 'db_table': "u'notesReceived'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'rolleventid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Rollevent']", 'db_column': "u'rollEventID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.page': {
            'Meta': {'object_name': 'Page', 'db_table': "u'page'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'referrerid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'referrerID'", 'blank': 'True'}),
            'showinmenu': ('django.db.models.fields.IntegerField', [], {'db_column': "u'showInMenu'"}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'null': 'True', 'db_column': "u'userID'", 'blank': 'True'})
        },
        u'migrate.pageaccounttype': {
            'Meta': {'object_name': 'Pageaccounttype', 'db_table': "u'pageAccountType'"},
            'accounttypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'accountTypeID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'pageid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'pageID'"})
        },
        u'migrate.period': {
            'Meta': {'object_name': 'Period', 'db_table': "u'period'"},
            'enddate': ('django.db.models.fields.DateField', [], {'db_column': "u'endDate'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'periodnumber': ('django.db.models.fields.IntegerField', [], {'db_column': "u'periodNumber'"}),
            'startdate': ('django.db.models.fields.DateField', [], {'db_column': "u'startDate'"}),
            'termid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Term']", 'db_column': "u'termID'"})
        },
        u'migrate.questionessays': {
            'Meta': {'object_name': 'QuestionEssays', 'db_table': "u'question_essays'"},
            'avclassid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'avClassID'"}),
            'essay': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'promptid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'promptID'", 'blank': 'True'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'termID'", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'traineeID'", 'blank': 'True'})
        },
        u'migrate.questionprompts': {
            'Meta': {'object_name': 'QuestionPrompts', 'db_table': "u'question_prompts'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'avclassid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'avClassID'", 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'mid_final': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '5000L'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'termID'", 'blank': 'True'})
        },
        u'migrate.recentupdates': {
            'Meta': {'object_name': 'Recentupdates', 'db_table': "u'recentUpdates'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '64L'})
        },
        u'migrate.recoveryweekday': {
            'Meta': {'object_name': 'Recoveryweekday', 'db_table': "u'recoveryWeekDay'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10L'})
        },
        u'migrate.reportcolumn': {
            'Meta': {'object_name': 'Reportcolumn', 'db_table': "u'reportColumn'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'displayorder': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'displayOrder'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'migrate.reportcolumnquery': {
            'Meta': {'object_name': 'Reportcolumnquery', 'db_table': "u'reportColumnQuery'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'reportcolumnid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Reportcolumn']", 'db_column': "u'reportColumnID'"}),
            'reportqueryid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Reportquery']", 'db_column': "u'reportQueryID'"})
        },
        u'migrate.reportquery': {
            'Meta': {'object_name': 'Reportquery', 'db_table': "u'reportQuery'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'query': ('django.db.models.fields.TextField', [], {})
        },
        u'migrate.requestcomment': {
            'Meta': {'object_name': 'Requestcomment', 'db_table': "u'requestComment'"},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'dateentered': ('django.db.models.fields.DateField', [], {'db_column': "u'dateEntered'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'requestid': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'requestID'"})
        },
        u'migrate.requesttracking': {
            'Meta': {'object_name': 'Requesttracking', 'db_table': "u'requestTracking'"},
            'actualenddate': ('django.db.models.fields.DateField', [], {'db_column': "u'actualEndDate'"}),
            'assignedto': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'assignedTo'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'proposedenddate': ('django.db.models.fields.DateField', [], {'db_column': "u'proposedEndDate'"}),
            'requester': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'startdate': ('django.db.models.fields.DateField', [], {'db_column': "u'startDate'"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'migrate.residence': {
            'Meta': {'object_name': 'Residence', 'db_table': "u'residence'"},
            'availablebeds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'availableBeds'", 'blank': 'True'}),
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'entrycode': ('django.db.models.fields.CharField', [], {'max_length': '11L', 'db_column': "u'entryCode'", 'blank': 'True'}),
            'fttause': ('django.db.models.fields.IntegerField', [], {'db_column': "u'fttaUse'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '24L', 'blank': 'True'}),
            'reportseq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'reportSeq'", 'blank': 'True'}),
            'residencetypeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'residenceTypeID'", 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2L', 'blank': 'True'}),
            'streetaddress': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'streetAddress'", 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'zipCode'", 'blank': 'True'})
        },
        u'migrate.residencerepairs': {
            'Meta': {'object_name': 'ResidenceRepairs', 'db_table': "u'residence_repairs'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'completed': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'other_room': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'residence_id': ('django.db.models.fields.IntegerField', [], {}),
            'room_id': ('django.db.models.fields.IntegerField', [], {}),
            'section_id': ('django.db.models.fields.IntegerField', [], {}),
            'trainee_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.residencerooms': {
            'Meta': {'object_name': 'ResidenceRooms', 'db_table': "u'residence_rooms'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'migrate.residenceroomsections': {
            'Meta': {'object_name': 'ResidenceRoomSections', 'db_table': "u'residence_room_sections'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'migrate.residencetype': {
            'Meta': {'object_name': 'Residencetype', 'db_table': "u'residenceType'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'residencetype': ('django.db.models.fields.CharField', [], {'max_length': '5L', 'db_column': "u'residenceType'"})
        },
        u'migrate.rolldata': {
            'Meta': {'object_name': 'Rolldata', 'db_table': "u'rollData'"},
            'enteredbyuserid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'null': 'True', 'db_column': "u'enteredByUserID'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'rolleventid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Rollevent']", 'db_column': "u'rollEventID'"}),
            'rollstatusid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Rollstatus']", 'db_column': "u'rollStatusID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.rollevent': {
            'Meta': {'object_name': 'Rollevent', 'db_table': "u'rollEvent'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'scheduleeventid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'scheduleEventID'"}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.rollhousefinalization': {
            'Meta': {'object_name': 'Rollhousefinalization', 'db_table': "u'rollhousefinalization'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'residenceID'"}),
            'submitdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submitDate'"}),
            'weekenddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'weekEndDate'"}),
            'weekstartdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'weekStartDate'"})
        },
        u'migrate.rollstatus': {
            'Meta': {'object_name': 'Rollstatus', 'db_table': "u'rollStatus'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15L'})
        },
        u'migrate.rollsubmissiondata': {
            'Meta': {'object_name': 'Rollsubmissiondata', 'db_table': "u'rollsubmissiondata'"},
            'enddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'endDate'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'startdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'startDate'"}),
            'submitdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submitDate'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.rollteamfinalization': {
            'Meta': {'object_name': 'Rollteamfinalization', 'db_table': "u'rollteamfinalization'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'submitdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submitDate'"}),
            'teamid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'teamID'"}),
            'weekenddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'weekEndDate'"}),
            'weekstartdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'weekStartDate'"})
        },
        u'migrate.rollypcfinalization': {
            'Meta': {'object_name': 'Rollypcfinalization', 'db_table': "u'rollypcfinalization'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'submitdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submitDate'"}),
            'weekenddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'weekEndDate'"}),
            'weekstartdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'weekStartDate'"})
        },
        u'migrate.room': {
            'Meta': {'object_name': 'Room', 'db_table': "u'room'"},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'residenceID'"})
        },
        u'migrate.roomlist': {
            'Meta': {'object_name': 'Roomlist', 'db_table': "u'roomlist'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'migrate.roomreservationrequests': {
            'Meta': {'object_name': 'Roomreservationrequests', 'db_table': "u'roomreservationrequests'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            'endtime': ('django.db.models.fields.TextField', [], {'db_column': "u'endTime'"}),
            'fellowshipwith': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'fellowshipWith'", 'blank': 'True'}),
            'frequency': ('django.db.models.fields.TextField', [], {}),
            'groupsize': ('django.db.models.fields.IntegerField', [], {'db_column': "u'groupSize'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'reminderflag': ('django.db.models.fields.IntegerField', [], {'db_column': "u'reminderFlag'"}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '11L'}),
            'starttime': ('django.db.models.fields.TextField', [], {'db_column': "u'startTime'"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.roomschedule': {
            'Meta': {'object_name': 'Roomschedule', 'db_table': "u'roomschedule'"},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'roomid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'roomID'"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'migrate.rsministrybooks': {
            'Meta': {'object_name': 'RsMinistrybooks', 'db_table': "u'rs_ministryBooks'"},
            'cartnumber': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'cartNumber'", 'blank': 'True'}),
            'code': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'migrate.rssyllabus': {
            'Meta': {'object_name': 'RsSyllabus', 'db_table': "u'rs_syllabus'"},
            'classtype': ('django.db.models.fields.CharField', [], {'max_length': '8L', 'db_column': "u'classType'"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'topic': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'trainingclassesid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'trainingClassesID'"})
        },
        u'migrate.rssyllabusreadings': {
            'Meta': {'object_name': 'RsSyllabusreadings', 'db_table': "u'rs_syllabusReadings'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'readings': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'rs_ministrybooksid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'rs_ministrybooksID'", 'blank': 'True'}),
            'rs_syllabusid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'rs_syllabusID'"})
        },
        u'migrate.savedreport': {
            'Meta': {'object_name': 'Savedreport', 'db_table': "u'savedReport'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'migrate.savedreportcolumn': {
            'Meta': {'object_name': 'Savedreportcolumn', 'db_table': "u'savedReportColumn'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'reportcolumnid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Reportcolumn']", 'db_column': "u'reportColumnID'"}),
            'savedreportid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Savedreport']", 'db_column': "u'savedReportID'"})
        },
        u'migrate.schedule': {
            'Meta': {'object_name': 'Schedule', 'db_table': "u'schedule'"},
            'accounttypeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Accounttype']", 'null': 'True', 'db_column': "u'accountTypeID'", 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'display': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'endDate'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'priority': ('django.db.models.fields.BigIntegerField', [], {}),
            'schedulecategoryid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'scheduleCategoryID'"}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'startDate'", 'blank': 'True'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"})
        },
        u'migrate.schedulecategory': {
            'Meta': {'object_name': 'Schedulecategory', 'db_table': "u'scheduleCategory'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'migrate.scheduleevent': {
            'Meta': {'object_name': 'Scheduleevent', 'db_table': "u'scheduleEvent'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'endtime': ('django.db.models.fields.TextField', [], {'db_column': "u'endTime'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'isclass': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isClass'"}),
            'isroll': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isRoll'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'blank': 'True'}),
            'scheduleid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Schedule']", 'db_column': "u'scheduleID'"}),
            'starttime': ('django.db.models.fields.TextField', [], {'db_column': "u'startTime'"}),
            'weekdayid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Weekday']", 'db_column': "u'weekDayID'"})
        },
        u'migrate.scheduletraineefilter': {
            'Meta': {'object_name': 'Scheduletraineefilter', 'db_table': "u'scheduleTraineeFilter'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'scheduleid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Schedule']", 'db_column': "u'scheduleID'"}),
            'traineefilterid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Traineefilter']", 'db_column': "u'traineeFilterID'"})
        },
        u'migrate.seat': {
            'Meta': {'object_name': 'Seat', 'db_table': "u'seat'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'seatingchartid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Seatingchart']", 'db_column': "u'seatingChartID'"}),
            'seatx': ('django.db.models.fields.IntegerField', [], {'db_column': "u'seatX'"}),
            'seaty': ('django.db.models.fields.IntegerField', [], {'db_column': "u'seatY'"})
        },
        u'migrate.seating': {
            'Meta': {'object_name': 'Seating', 'db_table': "u'seating'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'seatid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Seat']", 'db_column': "u'seatID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'null': 'True', 'db_column': "u'traineeID'", 'blank': 'True'})
        },
        u'migrate.seatingchart': {
            'Meta': {'object_name': 'Seatingchart', 'db_table': "u'seatingChart'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'seatingchartname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50L', 'db_column': "u'seatingChartName'"})
        },
        u'migrate.seatingevent': {
            'Meta': {'object_name': 'Seatingevent', 'db_table': "u'seatingEvent'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'scheduleeventid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Scheduleevent']", 'db_column': "u'scheduleEventID'"}),
            'seatingchartid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Seatingchart']", 'db_column': "u'seatingChartID'"})
        },
        u'migrate.semiannualstudyattendance': {
            'Meta': {'object_name': 'Semiannualstudyattendance', 'db_table': "u'semiAnnualStudyAttendance'"},
            'd1': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'd2': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'd3': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'd4': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'd5': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.semiannualstudylocation': {
            'Meta': {'object_name': 'Semiannualstudylocation', 'db_table': "u'semiAnnualStudyLocation'"},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '5L'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.semiannualtesting': {
            'Meta': {'object_name': 'Semiannualtesting', 'db_table': "u'semiAnnualTesting'"},
            'groupnumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'groupNumber'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'servicecode': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'serviceCode'", 'blank': 'True'}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.semiannualtestingrooms': {
            'Meta': {'object_name': 'Semiannualtestingrooms', 'db_table': "u'semiAnnualTestingRooms'"},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'groupnumber': ('django.db.models.fields.IntegerField', [], {'db_column': "u'groupNumber'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '1L'})
        },
        u'migrate.sendinglocality': {
            'Meta': {'object_name': 'Sendinglocality', 'db_table': "u'sendingLocality'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'localityid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'localityID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.svassignment': {
            'Meta': {'object_name': 'Svassignment', 'db_table': "u'svAssignment'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svscheduleinstanceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svscheduleinstance']", 'db_column': "u'svScheduleInstanceID'"}),
            'svserviceworkergroupid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svserviceworkergroup']", 'db_column': "u'svServiceWorkerGroupID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.svassignmentsave': {
            'Meta': {'object_name': 'Svassignmentsave', 'db_table': "u'svAssignmentSave'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svscheduleinstanceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svScheduleInstanceID'"}),
            'svserviceworkergroupid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceWorkerGroupID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.svexception': {
            'Meta': {'object_name': 'Svexception', 'db_table': "u'svException'"},
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'endDate'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'startDate'", 'blank': 'True'})
        },
        u'migrate.svexceptionservice': {
            'Meta': {'object_name': 'Svexceptionservice', 'db_table': "u'svExceptionService'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'svexceptionid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svExceptionID'", 'blank': 'True'}),
            'svserviceid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svServiceID'", 'blank': 'True'}),
            'svservicescheduleid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svServiceScheduleID'", 'blank': 'True'})
        },
        u'migrate.svexceptiontrainee': {
            'Meta': {'object_name': 'Svexceptiontrainee', 'db_table': "u'svExceptionTrainee'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'svexceptionid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svExceptionID'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'traineeID'", 'blank': 'True'})
        },
        u'migrate.svmissedservice': {
            'Meta': {'object_name': 'Svmissedservice', 'db_table': "u'svMissedService'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svscheduleinstanceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svScheduleInstanceID'"}),
            'svserviceworkergroupid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceWorkerGroupID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.svnote': {
            'Meta': {'object_name': 'Svnote', 'db_table': "u'svNote'"},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'moddate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'modDate'"}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'norder': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'null': 'True', 'db_column': "u'userID'", 'blank': 'True'})
        },
        u'migrate.svpermanentassignment': {
            'Meta': {'object_name': 'Svpermanentassignment', 'db_table': "u'svPermanentAssignment'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svserviceworkergroupid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svserviceworkergroup']", 'db_column': "u'svServiceWorkerGroupID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.svqualificationgroup': {
            'Meta': {'object_name': 'Svqualificationgroup', 'db_table': "u'svQualificationGroup'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'traineefilterid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Traineefilter']", 'db_column': "u'traineeFilterID'"})
        },
        u'migrate.svreport': {
            'Meta': {'object_name': 'Svreport', 'db_table': "u'svReport'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'headermessage': ('django.db.models.fields.TextField', [], {'db_column': "u'headerMessage'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'migrate.svreportnote': {
            'Meta': {'object_name': 'Svreportnote', 'db_table': "u'svReportNote'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'reporttype': ('django.db.models.fields.CharField', [], {'max_length': '511L', 'db_column': "u'reportType'", 'blank': 'True'})
        },
        u'migrate.svreportservice': {
            'Meta': {'object_name': 'Svreportservice', 'db_table': "u'svReportService'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'sortorder': ('django.db.models.fields.IntegerField', [], {'db_column': "u'sortOrder'"}),
            'svreportid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svReportID'"}),
            'svserviceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceID'"})
        },
        u'migrate.svreporttraineecomment': {
            'Meta': {'object_name': 'Svreporttraineecomment', 'db_table': "u'svReportTraineeComment'"},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svscheduleinstanceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svscheduleinstance']", 'db_column': "u'svScheduleInstanceID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.svrolldata': {
            'Meta': {'object_name': 'Svrolldata', 'db_table': "u'svRollData'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'isvolunteer': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isVolunteer'"}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'rollstatusid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Rollstatus']", 'db_column': "u'rollStatusID'"}),
            'substitutetraineeid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'svrolldata+'", 'db_column': "u'substituteTraineeID'", 'to': u"orm['migrate.Trainee']"}),
            'svrolleventid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svrollevent']", 'db_column': "u'svRollEventID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.svrollevent': {
            'Meta': {'object_name': 'Svrollevent', 'db_table': "u'svRollEvent'"},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'svservicetimeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svservicetime']", 'db_column': "u'svServiceTimeID'"}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'db_column': "u'userID'"})
        },
        u'migrate.svscheduleinstance': {
            'Meta': {'object_name': 'Svscheduleinstance', 'db_table': "u'svScheduleInstance'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'modifiedtime': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'modifiedTime'"}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'startDate'", 'blank': 'True'}),
            'svservicescheduleid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceScheduleID'"}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'null': 'True', 'db_column': "u'userID'", 'blank': 'True'})
        },
        u'migrate.svservice': {
            'Meta': {'object_name': 'Svservice', 'db_table': "u'svService'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'isactive': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isActive'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'svservicecategoryid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svservicecategory']", 'db_column': "u'svServiceCategoryID'"}),
            'svservicesorttypeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svservicesorttype']", 'db_column': "u'svServiceSortTypeID'"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'migrate.svservicealgorithm': {
            'Meta': {'object_name': 'Svservicealgorithm', 'db_table': "u'svServiceAlgorithm'"},
            'emphasis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svservicesorttypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceSortTypeID'"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'migrate.svservicecategory': {
            'Meta': {'object_name': 'Svservicecategory', 'db_table': "u'svServiceCategory'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'})
        },
        u'migrate.svserviceschedule': {
            'Meta': {'object_name': 'Svserviceschedule', 'db_table': "u'svServiceSchedule'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'})
        },
        u'migrate.svservicesorttype': {
            'Meta': {'object_name': 'Svservicesorttype', 'db_table': "u'svServiceSortType'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3L'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'migrate.svservicetime': {
            'Meta': {'object_name': 'Svservicetime', 'db_table': "u'svServiceTime'"},
            'endtime': ('django.db.models.fields.TextField', [], {'db_column': "u'endTime'", 'blank': 'True'}),
            'endtime2': ('django.db.models.fields.TextField', [], {'db_column': "u'endTime2'", 'blank': 'True'}),
            'endtime3': ('django.db.models.fields.TextField', [], {'db_column': "u'endTime3'", 'blank': 'True'}),
            'hidden_value2': ('django.db.models.fields.IntegerField', [], {}),
            'hidden_value3': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'recoverytime': ('django.db.models.fields.TextField', [], {'db_column': "u'recoveryTime'", 'blank': 'True'}),
            'recoveryweekdayid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'svservicetime'", 'db_column': "u'recoveryWeekDayID'", 'to': u"orm['migrate.Weekday']"}),
            'starttime': ('django.db.models.fields.TextField', [], {'db_column': "u'startTime'"}),
            'starttime2': ('django.db.models.fields.TextField', [], {'db_column': "u'startTime2'"}),
            'starttime3': ('django.db.models.fields.TextField', [], {'db_column': "u'startTime3'"}),
            'svserviceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svservice']", 'db_column': "u'svServiceID'"}),
            'svservicescheduleid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceScheduleID'"}),
            'week': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weekdayid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'svservicetime+'", 'db_column': "u'weekDayID'", 'to': u"orm['migrate.Weekday']"}),
            'weekdayid2': ('django.db.models.fields.IntegerField', [], {'db_column': "u'weekDayID2'"}),
            'weekdayid3': ('django.db.models.fields.IntegerField', [], {'db_column': "u'weekDayID3'"})
        },
        u'migrate.svservicetimescheduleevent': {
            'Meta': {'object_name': 'Svservicetimescheduleevent', 'db_table': "u'svServiceTimeScheduleEvent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheduleeventid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'scheduleEventID'"}),
            'svservicetimeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceTimeID'"})
        },
        u'migrate.svservicetoschedulemap': {
            'Meta': {'object_name': 'Svservicetoschedulemap', 'db_table': "u'svServiceToScheduleMap'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svserviceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceID'"}),
            'svservicescheduleid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceScheduleID'"})
        },
        u'migrate.svservicetraineefilter': {
            'Meta': {'object_name': 'Svservicetraineefilter', 'db_table': "u'svServiceTraineeFilter'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svserviceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svservice']", 'db_column': "u'svServiceID'"}),
            'traineefilterid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Traineefilter']", 'db_column': "u'traineeFilterID'"})
        },
        u'migrate.svserviceview': {
            'Meta': {'object_name': 'Svserviceview', 'db_table': "u'svserviceview'"},
            'categoryid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'categoryID'", 'blank': 'True'}),
            'categoryname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'db_column': "u'categoryName'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'isactive': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isActive'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'servicefilterid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'serviceFilterID'", 'blank': 'True'}),
            'servicefilterlookupid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'serviceFilterLookupID'", 'blank': 'True'}),
            'servicefiltername': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'serviceFilterName'", 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'workergrpfilterid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'workerGrpFilterID'", 'blank': 'True'}),
            'workergrpfilterlookupid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'workerGrpFilterLookupID'", 'blank': 'True'}),
            'workergrpfiltername': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'workerGrpFilterName'", 'blank': 'True'}),
            'workergrpid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'workerGrpID'", 'blank': 'True'}),
            'workergrpisactive': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'workerGrpIsActive'", 'blank': 'True'}),
            'workergrpname': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'db_column': "u'workerGrpName'", 'blank': 'True'}),
            'workergrpsuffix': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'workerGrpSuffix'", 'blank': 'True'})
        },
        u'migrate.svserviceweeklyreport': {
            'Meta': {'object_name': 'Svserviceweeklyreport', 'db_table': "u'svServiceWeeklyReport'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lastupdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'lastUpdate'"}),
            'svserviceid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceID'"}),
            'termid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'termID'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"}),
            'weekid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'weekID'"})
        },
        u'migrate.svserviceweeklyreportentry': {
            'Meta': {'object_name': 'Svserviceweeklyreportentry', 'db_table': "u'svServiceWeeklyReportEntry'"},
            'dayid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'dayID'"}),
            'endtime': ('django.db.models.fields.TextField', [], {'db_column': "u'endTime'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'starttime': ('django.db.models.fields.TextField', [], {'db_column': "u'startTime'", 'blank': 'True'}),
            'svserviceweeklyreportid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'svServiceWeeklyReportID'"}),
            'taskperformed': ('django.db.models.fields.TextField', [], {'db_column': "u'taskPerformed'", 'blank': 'True'})
        },
        u'migrate.svserviceworkergroup': {
            'Meta': {'object_name': 'Svserviceworkergroup', 'db_table': "u'svServiceWorkerGroup'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'isactive': ('django.db.models.fields.IntegerField', [], {'db_column': "u'isActive'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'numberofworkers': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numberOfWorkers'"}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10L'}),
            'svserviceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svservice']", 'db_column': "u'svServiceID'"}),
            'svservicescheduleid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svServiceScheduleID'", 'blank': 'True'})
        },
        u'migrate.svserviceworkergroupsnapshot': {
            'Meta': {'object_name': 'Svserviceworkergroupsnapshot', 'db_table': "u'svServiceWorkerGroupSnapshot'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'numberofworkers': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numberOfWorkers'"}),
            'svscheduleinstanceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svscheduleinstance']", 'db_column': "u'svScheduleInstanceID'"}),
            'svserviceworkergroupid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svserviceworkergroup']", 'db_column': "u'svServiceWorkerGroupID'"})
        },
        u'migrate.svserviceworkergrouptraineefilter': {
            'Meta': {'object_name': 'Svserviceworkergrouptraineefilter', 'db_table': "u'svServiceWorkerGroupTraineeFilter'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svserviceworkergroupid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svserviceworkergroup']", 'db_column': "u'svServiceWorkerGroupID'"}),
            'traineefilterid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Traineefilter']", 'db_column': "u'traineeFilterID'"})
        },
        u'migrate.svworkerexception': {
            'Meta': {'object_name': 'Svworkerexception', 'db_table': "u'svWorkerException'"},
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'endDate'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {'db_column': "u'startDate'"}),
            'svserviceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svservice']", 'null': 'True', 'db_column': "u'svServiceID'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.svworkerqualification': {
            'Meta': {'object_name': 'Svworkerqualification', 'db_table': "u'svWorkerQualification'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'svqualificationgroupid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Svqualificationgroup']", 'db_column': "u'svQualificationGroupID'"}),
            'traineeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainee']", 'db_column': "u'traineeID'"})
        },
        u'migrate.svworkloadhistory': {
            'Meta': {'object_name': 'Svworkloadhistory', 'db_table': "u'svWorkloadHistory'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'oldworkload': ('django.db.models.fields.IntegerField', [], {'db_column': "u'oldWorkload'"}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.team': {
            'Meta': {'object_name': 'Team', 'db_table': "u'team'"},
            'bromonitortraineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'broMonitorTraineeID'"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'sismonitortraineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'sisMonitorTraineeID'"}),
            'teamtypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'teamTypeID'"}),
            'trainerusername': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'db_column': "u'trainerUserName'"})
        },
        u'migrate.teamschedule': {
            'Meta': {'object_name': 'Teamschedule', 'db_table': "u'teamSchedule'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'scheduleid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'scheduleID'"}),
            'teamid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'teamID'"})
        },
        u'migrate.teamtype': {
            'Meta': {'object_name': 'Teamtype', 'db_table': "u'teamType'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"})
        },
        u'migrate.term': {
            'Meta': {'object_name': 'Term', 'db_table': "u'term'"},
            'enddate': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'endDate'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45L'}),
            'startdate': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'db_column': "u'startDate'"}),
            'taskscompleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'tasksCompleted'", 'blank': 'True'}),
            'taskstage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'taskStage'", 'blank': 'True'})
        },
        u'migrate.tmplsimportoffense': {
            'Meta': {'object_name': 'Tmplsimportoffense', 'db_table': "u'tmpLsImportOffense'"},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'datedue': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'DateDue'", 'blank': 'True'}),
            'dns': ('django.db.models.fields.IntegerField', [], {'db_column': "u'DNS'"}),
            'fullyturnedin': ('django.db.models.fields.IntegerField', [], {'db_column': "u'FullyTurnedIn'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'importsignedin': ('django.db.models.fields.IntegerField', [], {'db_column': "u'importSignedIn'"}),
            'lastfirst': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'lastFirst'"}),
            'lastupdatedate': ('django.db.models.fields.DateField', [], {'db_column': "u'lastUpdateDate'"}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '7L'}),
            'manualhandling': ('django.db.models.fields.IntegerField', [], {'db_column': "u'manualHandling'"}),
            'numlsowed': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numLSOwed'"}),
            'numlsreceived': ('django.db.models.fields.IntegerField', [], {'db_column': "u'numLSReceived'"}),
            'offensereason': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'db_column': "u'offenseReason'"}),
            'snc': ('django.db.models.fields.IntegerField', [], {'db_column': "u'SNC'"}),
            'wnr': ('django.db.models.fields.IntegerField', [], {'db_column': "u'WNR'"})
        },
        u'migrate.trainee': {
            'Meta': {'object_name': 'Trainee', 'db_table': "u'trainee'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'bunkid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'bunkID'", 'blank': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'couple': ('django.db.models.fields.IntegerField', [], {}),
            'datebegin': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dateBegin'", 'blank': 'True'}),
            'dateend': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dateEnd'", 'blank': 'True'}),
            'degree': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergencyaddress': ('django.db.models.fields.TextField', [], {'db_column': "u'emergencyAddress'", 'blank': 'True'}),
            'emergencycontact': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'emergencyContact'", 'blank': 'True'}),
            'emergencyphonenumber': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'emergencyPhoneNumber'", 'blank': 'True'}),
            'emergencyphonenumber2': ('django.db.models.fields.CharField', [], {'max_length': '14L', 'db_column': "u'emergencyPhoneNumber2'", 'blank': 'True'}),
            'firstterm_termid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Term']", 'null': 'True', 'db_column': "u'firstTerm_termID'", 'blank': 'True'}),
            'fourthterm_termid': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'trainee+'", 'null': 'True', 'db_column': "u'fourthTerm_termID'", 'to': u"orm['migrate.Term']"}),
            'gospelpreference1': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'gospelPreference1'", 'blank': 'True'}),
            'gospelpreference2': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'gospelPreference2'", 'blank': 'True'}),
            'greekcharacter': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'mentor': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'mentor_userid': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'trainee'", 'null': 'True', 'db_column': "u'mentor_userID'", 'to': u"orm['migrate.User']"}),
            'mrtype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MRType'", 'blank': 'True'}),
            'officeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'officeID'", 'blank': 'True'}),
            'readnewtestament': ('django.db.models.fields.IntegerField', [], {'db_column': "u'readNewTestament'"}),
            'readoldtestament': ('django.db.models.fields.IntegerField', [], {'db_column': "u'readOldTestament'"}),
            'residenceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Residence']", 'null': 'True', 'db_column': "u'residenceID'", 'blank': 'True'}),
            'secondterm_termid': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'trainee+'", 'null': 'True', 'db_column': "u'secondTerm_termID'", 'to': u"orm['migrate.Term']"}),
            'svservicesleft': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svServicesLeft'", 'blank': 'True'}),
            'teamid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'teamID'", 'blank': 'True'}),
            'termscompleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'termsCompleted'", 'blank': 'True'}),
            'thirdterm_termid': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'trainee+'", 'null': 'True', 'db_column': "u'thirdTerm_termID'", 'to': u"orm['migrate.Term']"}),
            'traineestatusid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Traineestatus']", 'db_column': "u'traineeStatusID'"}),
            'trainingassistantid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Trainingassistant']", 'null': 'True', 'db_column': "u'trainingAssistantID'", 'blank': 'True'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'trainee+'", 'null': 'True', 'db_column': "u'userID'", 'to': u"orm['migrate.User']", 'blank': 'True', 'unique': 'True'}),
            'vehiclecapacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'vehicleCapacity'", 'blank': 'True'}),
            'vehiclecolor': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleColor'", 'blank': 'True'}),
            'vehicleinfoold': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleInfoOld'", 'blank': 'True'}),
            'vehiclelicense': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleLicense'", 'blank': 'True'}),
            'vehiclemakeold': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'vehicleMakeOld'", 'blank': 'True'}),
            'vehiclemodel': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleModel'", 'blank': 'True'}),
            'vehiclemodelold': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'vehicleModelOld'", 'blank': 'True'}),
            'vehicleyearold': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'vehicleYearOld'", 'blank': 'True'}),
            'vehicleyesno': ('django.db.models.fields.IntegerField', [], {'db_column': "u'vehicleYesNo'"})
        },
        u'migrate.traineefilter': {
            'Meta': {'object_name': 'Traineefilter', 'db_table': "u'traineeFilter'"},
            'filter': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L'})
        },
        u'migrate.traineeold': {
            'Meta': {'object_name': 'TraineeOld', 'db_table': "u'trainee_old'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'birthDate'", 'blank': 'True'}),
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'db_column': "u'cellPhone'", 'blank': 'True'}),
            'datebegin': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dateBegin'", 'blank': 'True'}),
            'dateend': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dateEnd'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.TextField', [], {'db_column': "u'firstName'"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lastname': ('django.db.models.fields.TextField', [], {'db_column': "u'lastName'"}),
            'maritalstatus': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'maritalStatus'", 'blank': 'True'}),
            'middlename': ('django.db.models.fields.TextField', [], {'db_column': "u'middleName'", 'blank': 'True'}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'residenceID'", 'blank': 'True'}),
            'sendinglocality': ('django.db.models.fields.TextField', [], {'db_column': "u'sendingLocality'", 'blank': 'True'}),
            'teamid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'teamID'", 'blank': 'True'}),
            'termscompleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'termsCompleted'", 'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'db_column': "u'userID'", 'blank': 'True'})
        },
        u'migrate.traineeschedule': {
            'Meta': {'object_name': 'Traineeschedule', 'db_table': "u'traineeSchedule'"},
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'endDate'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'scheduleid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Schedule']", 'db_column': "u'scheduleID'"}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'startDate'", 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeID'"})
        },
        u'migrate.traineestatus': {
            'Meta': {'object_name': 'Traineestatus', 'db_table': "u'traineeStatus'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'migrate.traineeview': {
            'Meta': {'object_name': 'Traineeview', 'db_table': "u'traineeview'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'birthDate'", 'blank': 'True'}),
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '14L', 'db_column': "u'cellPhone'", 'blank': 'True'}),
            'couple': ('django.db.models.fields.IntegerField', [], {}),
            'datebegin': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dateBegin'", 'blank': 'True'}),
            'dateend': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'dateEnd'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'firstName'"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'greekcharacter': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lastfirst': ('django.db.models.fields.CharField', [], {'max_length': '66L', 'db_column': "u'lastFirst'"}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'lastName'"}),
            'maritalstatus': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'maritalStatus'", 'blank': 'True'}),
            'middlename': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'middleName'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '65L'}),
            'officeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'officeID'", 'blank': 'True'}),
            'residenceid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'residenceID'", 'blank': 'True'}),
            'residencename': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'residenceName'", 'blank': 'True'}),
            'sendinglocality': ('django.db.models.fields.TextField', [], {'db_column': "u'sendingLocality'", 'blank': 'True'}),
            'svservicesleft': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'svServicesLeft'", 'blank': 'True'}),
            'teamcode': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'db_column': "u'teamCode'", 'blank': 'True'}),
            'teamid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'teamID'", 'blank': 'True'}),
            'teamname': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'teamName'", 'blank': 'True'}),
            'teamtrainer': ('django.db.models.fields.CharField', [], {'max_length': '45L', 'db_column': "u'teamTrainer'", 'blank': 'True'}),
            'teamtype': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'db_column': "u'teamType'", 'blank': 'True'}),
            'teamtypeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'teamTypeID'", 'blank': 'True'}),
            'termscompleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'termsCompleted'", 'blank': 'True'}),
            'traineestatus': ('django.db.models.fields.TextField', [], {'db_column': "u'traineeStatus'", 'blank': 'True'}),
            'traineestatusid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'traineeStatusID'"}),
            'trainingassistantid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'trainingAssistantID'", 'blank': 'True'}),
            'trainingassistantname': ('django.db.models.fields.CharField', [], {'max_length': '65L', 'db_column': "u'trainingAssistantName'", 'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '32L'}),
            'vehiclecapacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'vehicleCapacity'", 'blank': 'True'}),
            'vehiclecolor': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleColor'", 'blank': 'True'}),
            'vehicleinfo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'vehicleInfo'", 'blank': 'True'}),
            'vehiclelicense': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleLicense'", 'blank': 'True'}),
            'vehiclemake': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleMake'", 'blank': 'True'}),
            'vehiclemodel': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleModel'", 'blank': 'True'}),
            'vehicleyear': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'db_column': "u'vehicleYear'", 'blank': 'True'})
        },
        u'migrate.trainingassistant': {
            'Meta': {'object_name': 'Trainingassistant', 'db_table': "u'trainingAssistant'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'approvingtaid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'approvingTAID'", 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'birthDate'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'firstName'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'lastName'"}),
            'maritalstatus': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'maritalStatus'", 'blank': 'True'}),
            'middlename': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'middleName'", 'blank': 'True'}),
            'outoftown': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'outOfTown'", 'blank': 'True'}),
            'residence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'db_column': "u'userID'"})
        },
        u'migrate.trainingassistantview': {
            'Meta': {'object_name': 'Trainingassistantview', 'db_table': "u'trainingassistantview'"},
            'approvingtaid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'approvingTAID'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'firstName'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lastfirst': ('django.db.models.fields.CharField', [], {'max_length': '66L', 'db_column': "u'lastFirst'"}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'lastName'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '65L'}),
            'outoftown': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'outOfTown'", 'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.trainingclasses': {
            'Meta': {'object_name': 'Trainingclasses', 'db_table': "u'trainingClasses'"},
            'code': ('django.db.models.fields.TextField', [], {}),
            'hassyllabus': ('django.db.models.fields.IntegerField', [], {'db_column': "u'hasSyllabus'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'readwhen': ('django.db.models.fields.IntegerField', [], {'db_column': "u'readWhen'"}),
            'secode': ('django.db.models.fields.TextField', [], {'db_column': "u'seCode'"}),
            'weekdayid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'weekdayID'"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '6L'})
        },
        u'migrate.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'user'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "u'birthDate'", 'blank': 'True'}),
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '14L', 'db_column': "u'cellPhone'", 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'encryptedpassword': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'encryptedPassword'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'firstName'"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'home_localityid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'home_localityID'", 'blank': 'True'}),
            'homephone': ('django.db.models.fields.CharField', [], {'max_length': '14L', 'db_column': "u'homePhone'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lastip': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'db_column': "u'lastIP'", 'blank': 'True'}),
            'lastlogin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'lastLogin'", 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'lastName'"}),
            'maidenname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'maidenName'", 'blank': 'True'}),
            'maritalstatus': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'db_column': "u'maritalStatus'", 'blank': 'True'}),
            'middlename': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'middleName'", 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'nickName'", 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32L'}),
            'workphone': ('django.db.models.fields.TextField', [], {'db_column': "u'workPhone'", 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'})
        },
        u'migrate.useraccounttype': {
            'Meta': {'object_name': 'Useraccounttype', 'db_table': "u'userAccountType'"},
            'accounttypeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.Accounttype']", 'db_column': "u'accountTypeID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['migrate.User']", 'db_column': "u'userID'"})
        },
        u'migrate.waapprovalstatus': {
            'Meta': {'object_name': 'Waapprovalstatus', 'db_table': "u'waApprovalStatus'"},
            'approvalstatus': ('django.db.models.fields.CharField', [], {'max_length': '12L', 'db_column': "u'approvalStatus'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"})
        },
        u'migrate.wamaclist': {
            'Meta': {'object_name': 'Wamaclist', 'db_table': "u'waMACList'"},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '17L'}),
            'userid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'userID'"})
        },
        u'migrate.wareason': {
            'Meta': {'object_name': 'Wareason', 'db_table': "u'waReason'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '32L'})
        },
        u'migrate.warequest': {
            'Meta': {'object_name': 'Warequest', 'db_table': "u'waRequest'"},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '17L', 'db_column': "u'MAC'"}),
            'minutes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'submissiondate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'submissionDate'"}),
            'tacomments': ('django.db.models.fields.TextField', [], {'db_column': "u'TAComments'", 'blank': 'True'}),
            'timestart': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'traineeid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'traineeID'", 'blank': 'True'}),
            'usagedate': ('django.db.models.fields.DateField', [], {'db_column': "u'usageDate'"}),
            'usagetime': ('django.db.models.fields.TextField', [], {'db_column': "u'usageTime'", 'blank': 'True'}),
            'waapprovalstatusid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'waApprovalStatusID'"}),
            'wareasonid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'waReasonID'"})
        },
        u'migrate.weatherlocation': {
            'Meta': {'object_name': 'Weatherlocation', 'db_table': "u'weatherLocation'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'cache': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '4', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '4', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32L'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5L'})
        },
        u'migrate.weekday': {
            'Meta': {'object_name': 'Weekday', 'db_table': "u'weekDay'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'dayorder': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'dayOrder'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10L'})
        }
    }

    complete_apps = ['migrate']