# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Vehicle(models.Model):

    color = models.CharField(max_length=10)

    # e.g. "Honda", "Toyota"
    make = models.CharField(max_length=30)

    # e.g. "Accord", "Camry"
    model = models.CharField(max_length=30)

    license_plate = models.CharField(max_length=10)

    state = models.CharField(max_length=20)

    # TODO Same as above
    trainee = models.OneToOneField('Trainee', blank=True, null=True)

    def __unicode__(self):
        return self.color + ' ' + self.make + ' ' + self.model

class Hcrecmd(models.Model):
    residenceid = models.IntegerField(db_column='ResidenceID') # Field name made lowercase.
    hcuserid = models.IntegerField(db_column='HCUserID') # Field name made lowercase.
    recmdhcuserid = models.IntegerField(db_column='recmdHCUserID') # Field name made lowercase.
    choice = models.IntegerField()
    evalcriterion1 = models.IntegerField(db_column='evalCriterion1') # Field name made lowercase.
    evalcriterion2 = models.IntegerField(db_column='evalCriterion2') # Field name made lowercase.
    evalcriterion3 = models.IntegerField(db_column='evalCriterion3') # Field name made lowercase.
    evalcriterion4 = models.IntegerField(db_column='evalCriterion4') # Field name made lowercase.
    evalcriterion5 = models.IntegerField(db_column='evalCriterion5') # Field name made lowercase.
    evalcriterion6 = models.IntegerField(db_column='evalCriterion6') # Field name made lowercase.
    evalcriterion7 = models.IntegerField(db_column='evalCriterion7') # Field name made lowercase.
    evalcriterion8 = models.IntegerField(db_column='evalCriterion8') # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    class Meta:
        db_table = 'HCRecmd'

class Hcrecmdcriteria(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    description = models.CharField(max_length=50L)
    min = models.CharField(max_length=50L, blank=True)
    max = models.CharField(max_length=50L, blank=True)
    class Meta:
        db_table = 'HCRecmdCriteria'

class Accounttype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L, unique=True)
    code = models.CharField(max_length=3L, unique=True)
    databasetable = models.CharField(max_length=255L, db_column='databaseTable', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'accountType'

class Announcementmember(models.Model):
    announcementrequestid = models.IntegerField(db_column='announcementRequestID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    viewed = models.CharField(max_length=3L)
    class Meta:
        db_table = 'announcementMember'

class Announcementrequest(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    announcementtypeid = models.IntegerField(db_column='announcementTypeID') # Field name made lowercase.
    typevalue = models.TextField(db_column='typeValue', blank=True) # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='dateCreated') # Field name made lowercase.
    announcement = models.TextField()
    purpose = models.TextField()
    date2announce = models.DateField(db_column='date2Announce') # Field name made lowercase.
    date2hide = models.DateTimeField(null=True, db_column='date2Hide', blank=True) # Field name made lowercase.
    announcementstatusid = models.IntegerField(db_column='announcementStatusID') # Field name made lowercase.
    showpaper = models.IntegerField(db_column='showPaper') # Field name made lowercase.
    showserver = models.IntegerField(db_column='showServer') # Field name made lowercase.
    showcommons = models.IntegerField(db_column='showCommons') # Field name made lowercase.
    tacomments = models.TextField(db_column='TAComments', blank=True) # Field name made lowercase.
    ta_userid = models.IntegerField(null=True, db_column='ta_userID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'announcementRequest'

class Announcementselection(models.Model):
    announcementrequestid = models.IntegerField(db_column='announcementRequestID') # Field name made lowercase.
    foreignid = models.IntegerField(db_column='foreignID') # Field name made lowercase.
    class Meta:
        db_table = 'announcementSelection'

class Announcementstatus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100L)
    class Meta:
        db_table = 'announcementStatus'

class Announcementtype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100L)
    class Meta:
        db_table = 'announcementType'

class Atrabsenttrainee(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    atrrosterid = models.IntegerField(db_column='atrRosterID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    reason = models.CharField(max_length=17L)
    details = models.CharField(max_length=255L, blank=True)
    numdays = models.IntegerField(null=True, db_column='numDays', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'atrAbsentTrainee'

class Atrroster(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    date = models.DateField(unique=True)
    notes = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'atrRoster'

class Atrunreportedhouse(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    atrrosterid = models.IntegerField(db_column='atrRosterID') # Field name made lowercase.
    residenceid = models.IntegerField(db_column='residenceID') # Field name made lowercase.
    class Meta:
        db_table = 'atrUnreportedHouse'

class Attendancesystem(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100L, unique=True)
    code = models.CharField(max_length=3L, unique=True)
    comments = models.CharField(max_length=100L, blank=True)
    term1 = models.IntegerField(null=True, blank=True)
    term2 = models.IntegerField(null=True, blank=True)
    term3 = models.IntegerField(null=True, blank=True)
    term4 = models.IntegerField(null=True, blank=True)
    enabled = models.IntegerField()
    class Meta:
        db_table = 'attendancesystem'

class Attendancetables(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    tablename = models.CharField(max_length=10L, db_column='tableName') # Field name made lowercase.
    class Meta:
        db_table = 'attendancetables'

class Avapprovalstatus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    approvalstatus = models.CharField(max_length=100L, db_column='approvalStatus') # Field name made lowercase.
    class Meta:
        db_table = 'avApprovalStatus'

class Avclass(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100L)
    code = models.CharField(max_length=10L)
    classyear = models.IntegerField(db_column='classYear') # Field name made lowercase.
    dayofweek = models.CharField(max_length=100L, db_column='dayOfWeek') # Field name made lowercase.
    scheduleeventname = models.CharField(max_length=45L, db_column='scheduleEventName') # Field name made lowercase.
    class Meta:
        db_table = 'avClass'

class Avreason(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    reason = models.CharField(max_length=100L)
    class Meta:
        db_table = 'avReason'

class Avrequest(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    avclassid = models.IntegerField(db_column='avClassID') # Field name made lowercase.
    classdate = models.DateField(db_column='classDate') # Field name made lowercase.
    avreasonid = models.IntegerField(db_column='avReasonID') # Field name made lowercase.
    datesubmitted = models.DateField(db_column='dateSubmitted') # Field name made lowercase.
    avapprovalstatusid = models.IntegerField(db_column='avApprovalStatusID') # Field name made lowercase.
    dateapproved = models.DateField(null=True, db_column='dateApproved', blank=True) # Field name made lowercase.
    avrequestcommentid = models.IntegerField(null=True, db_column='avRequestCommentID', blank=True) # Field name made lowercase.
    tacomments = models.TextField(db_column='TAComments', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'avRequest'

class Avrequestcomment(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True) # Field name made lowercase.
    ta_userid = models.IntegerField(null=True, db_column='ta_userID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'avRequestComment'

class Bostonapp(models.Model):
    application_id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    submitted = models.IntegerField()
    trainee_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100L, blank=True)
    sending_locality = models.CharField(max_length=100L, blank=True)
    gender = models.CharField(max_length=10L, blank=True)
    birth_date = models.TextField(blank=True)
    age = models.TextField(blank=True)
    citizenship = models.TextField(blank=True)
    citizenship_other = models.TextField(blank=True)
    address = models.TextField(blank=True)
    city = models.TextField(blank=True)
    state = models.TextField(blank=True)
    zip = models.TextField(blank=True)
    lang_chinese = models.TextField(blank=True)
    lang_spanish = models.TextField(blank=True)
    lang_korean = models.TextField(blank=True)
    lang_other = models.TextField(blank=True)
    bicycle = models.TextField(blank=True)
    automobile = models.TextField(blank=True)
    automobile_seats = models.TextField(blank=True)
    phone_cell = models.TextField(blank=True)
    phone_home = models.TextField(blank=True)
    email = models.TextField(blank=True)
    english_ability = models.TextField(blank=True)
    college1 = models.TextField(blank=True)
    major1 = models.TextField(blank=True)
    degree1 = models.TextField(blank=True)
    college2 = models.TextField(blank=True)
    major2 = models.TextField(blank=True)
    degree2 = models.TextField(blank=True)
    date_saved = models.TextField(blank=True)
    date_baptized = models.TextField(blank=True)
    first_locality = models.TextField(blank=True)
    first_locality_date = models.TextField(blank=True)
    service_areas = models.TextField(blank=True)
    previous_training = models.TextField(blank=True)
    previous_training_graduation_date = models.TextField(blank=True)
    marital_status = models.TextField(blank=True)
    spouse_name = models.TextField(blank=True)
    spouse_occupation = models.TextField(blank=True)
    spouse_age = models.TextField(blank=True)
    marriage_date = models.TextField(blank=True)
    spouse_attitude = models.TextField(blank=True)
    dependents = models.TextField(blank=True)
    support_yourself = models.TextField(blank=True)
    support_church = models.TextField(blank=True)
    support_family_friends = models.TextField(blank=True)
    support_other = models.TextField(blank=True)
    other_info = models.TextField(blank=True)
    statement = models.TextField(blank=True)
    class Meta:
        db_table = 'bostonApp'

class BrBooks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30L)
    class Meta:
        db_table = 'br_books'

class BrTraineeBook(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(BrBooks)
    trainee = models.ForeignKey('Trainee')
    term = models.ForeignKey('Term')
    class Meta:
        db_table = 'br_trainee_book'

class Bugs(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    assignedto_userid = models.IntegerField(null=True, db_column='assignedTo_userID', blank=True) # Field name made lowercase.
    datestarted = models.CharField(max_length=10L, db_column='dateStarted') # Field name made lowercase.
    projecteddate = models.CharField(max_length=10L, db_column='projectedDate') # Field name made lowercase.
    datecompleted = models.CharField(max_length=10L, db_column='dateCompleted') # Field name made lowercase.
    pageid = models.IntegerField(db_column='pageID') # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='timeStamp') # Field name made lowercase.
    bug = models.TextField(blank=True)
    isdone = models.IntegerField(db_column='isDone') # Field name made lowercase.
    isvisible = models.CharField(max_length=3L, db_column='isVisible') # Field name made lowercase.
    priority = models.IntegerField(null=True, blank=True)
    useragent = models.TextField(db_column='userAgent', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'bugs'

class Bunk(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    roomid = models.IntegerField(db_column='roomID') # Field name made lowercase.
    bunkno = models.CharField(max_length=8L, db_column='bunkNo', blank=True) # Field name made lowercase.
    type = models.CharField(max_length=6L, blank=True)
    bunkid = models.IntegerField(null=True, db_column='bunkID', blank=True) # Field name made lowercase.
    length = models.IntegerField(null=True, blank=True)
    fttause = models.IntegerField(null=True, db_column='fttaUse', blank=True) # Field name made lowercase.
    notes = models.TextField(blank=True)
    class Meta:
        db_table = 'bunk'

class Church(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    active = models.IntegerField()
    class Meta:
        db_table = 'church'

class Classnotes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    rolleventid = models.ForeignKey('Rollevent', null=True, db_column='rollEventID', blank=True) # Field name made lowercase.
    submissiondate = models.DateTimeField(db_column='submissionDate') # Field name made lowercase.
    text = models.TextField()
    finalized = models.IntegerField()
    class Meta:
        db_table = 'classNotes'

class Conference(models.Model):
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    allergies = models.TextField()
    housing = models.IntegerField()
    paid = models.IntegerField()
    comments = models.TextField(blank=True)
    class Meta:
        db_table = 'conference'

class Dailybibleverse(models.Model):
    id = models.IntegerField(primary_key=True)
    verseref = models.CharField(max_length=30L, db_column='verseRef') # Field name made lowercase.
    verse = models.TextField()
    dateadded = models.DateField(db_column='dateAdded') # Field name made lowercase.
    lastdisplayed = models.DateTimeField(null=True, db_column='lastDisplayed', blank=True) # Field name made lowercase.
    isdisplayed = models.IntegerField(db_column='isDisplayed') # Field name made lowercase.
    class Meta:
        db_table = 'dailyBibleVerse'

class Dberror(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    file = models.CharField(max_length=128L)
    line = models.IntegerField()
    bugsid = models.IntegerField(db_column='bugsID') # Field name made lowercase.
    timestamp = models.DateTimeField()
    logpageid = models.IntegerField(null=True, db_column='logPageID', blank=True) # Field name made lowercase.
    error = models.TextField()
    query = models.TextField()
    stacktrace = models.TextField(db_column='stackTrace') # Field name made lowercase.
    class Meta:
        db_table = 'dbError'

class Exams(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    trainingclassesid = models.IntegerField(db_column='trainingClassesID') # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime') # Field name made lowercase.
    type = models.TextField(blank=True)
    last_updated = models.DateTimeField()
    exam = models.TextField()
    status = models.CharField(max_length=8L)
    class Meta:
        db_table = 'exams'

class Examstraineeaccess(models.Model):
    examid = models.IntegerField(db_column='examID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    class Meta:
        db_table = 'examsTraineeAccess'

class Examstraineeanswers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='lastUpdated') # Field name made lowercase.
    examid = models.IntegerField(db_column='examID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    answers = models.TextField()
    grade = models.IntegerField(null=True, blank=True)
    finalized = models.IntegerField()
    class Meta:
        db_table = 'examsTraineeAnswers'

class Examstraineeanswersgrades(models.Model):
    examstraineeanswersid = models.IntegerField(db_column='examsTraineeAnswersID') # Field name made lowercase.
    questionnumber = models.IntegerField(db_column='questionNumber') # Field name made lowercase.
    points = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=300L, blank=True)
    class Meta:
        db_table = 'examsTraineeAnswersGrades'

class FrameRequests(models.Model):
    id = models.IntegerField(primary_key=True)
    residence_id = models.IntegerField()
    trainee_id = models.IntegerField()
    location = models.TextField()
    exists_already = models.IntegerField()
    fix = models.IntegerField(null=True, blank=True)
    broken_text = models.TextField(blank=True)
    frame_quote = models.TextField()
    completed = models.IntegerField()
    completed_date = models.DateField()
    created_at = models.DateTimeField()
    active = models.IntegerField()
    notes = models.TextField()
    priority = models.IntegerField()
    class Meta:
        db_table = 'frame_requests'

class Globalsettings(models.Model):
    name = models.CharField(max_length=32L, primary_key=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = 'globalSettings'

class Gospelcitizenship(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    citizenship = models.CharField(max_length=100L)
    class Meta:
        db_table = 'gospelCitizenship'

class Gospelsurvey(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    name = models.CharField(max_length=40L)
    term = models.IntegerField()
    options = models.CharField(max_length=40L)
    reason = models.CharField(max_length=100L, blank=True)
    year = models.CharField(max_length=40L)
    class Meta:
        db_table = 'gospelSurvey'

class Gospeltripapplication(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    pref1 = models.CharField(max_length=200L, blank=True)
    preftext1 = models.TextField(db_column='prefText1', blank=True) # Field name made lowercase.
    car1 = models.CharField(max_length=3L, blank=True)
    pref2 = models.CharField(max_length=100L, blank=True)
    preftext2 = models.TextField(db_column='prefText2', blank=True) # Field name made lowercase.
    car2 = models.CharField(max_length=3L, blank=True)
    pref3 = models.CharField(max_length=100L, blank=True)
    preftext3 = models.TextField(db_column='prefText3', blank=True) # Field name made lowercase.
    car3 = models.CharField(max_length=3L, blank=True)
    pref4 = models.CharField(max_length=100L, blank=True)
    preftext4 = models.TextField(db_column='prefText4', blank=True) # Field name made lowercase.
    car4 = models.CharField(max_length=3L, blank=True)
    pref5 = models.CharField(max_length=100L, blank=True)
    preftext5 = models.TextField(db_column='prefText5', blank=True) # Field name made lowercase.
    car5 = models.CharField(max_length=3L, blank=True)
    pref6 = models.CharField(max_length=100L, blank=True)
    preftext6 = models.TextField(db_column='prefText6', blank=True) # Field name made lowercase.
    car6 = models.CharField(max_length=3L, blank=True)
    lang1 = models.CharField(max_length=100L, blank=True)
    prof1 = models.CharField(max_length=100L, blank=True)
    langtext1 = models.TextField(db_column='langText1', blank=True) # Field name made lowercase.
    lang2 = models.CharField(max_length=100L, blank=True)
    prof2 = models.CharField(max_length=100L, blank=True)
    langtext2 = models.TextField(db_column='langText2', blank=True) # Field name made lowercase.
    lang3 = models.CharField(max_length=100L, blank=True)
    prof3 = models.CharField(max_length=100L, blank=True)
    langtext3 = models.TextField(db_column='langText3', blank=True) # Field name made lowercase.
    lang4 = models.CharField(max_length=100L, blank=True)
    prof4 = models.CharField(max_length=100L, blank=True)
    langtext4 = models.TextField(db_column='langText4', blank=True) # Field name made lowercase.
    lang5 = models.CharField(max_length=100L, blank=True)
    prof5 = models.CharField(max_length=100L, blank=True)
    langtext5 = models.TextField(db_column='langText5', blank=True) # Field name made lowercase.
    lang6 = models.CharField(max_length=100L, blank=True)
    prof6 = models.CharField(max_length=100L, blank=True)
    langtext6 = models.TextField(db_column='langText6', blank=True) # Field name made lowercase.
    show = models.IntegerField()
    class Meta:
        db_table = 'gospelTripApplication'

class Gospeltriparrangement(models.Model):
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    gospeltriprunid = models.ForeignKey('Gospeltriprun', db_column='gospelTripRunID') # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripArrangement'

class Gospeltripassignment(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    deposit = models.CharField(max_length=10L, blank=True)
    balance = models.CharField(max_length=10L, blank=True)
    balancepaid = models.DateField(null=True, db_column='balancePaid', blank=True) # Field name made lowercase.
    gospeltripdestinationid = models.IntegerField(null=True, db_column='gospelTripDestinationID', blank=True) # Field name made lowercase.
    comments = models.CharField(max_length=200L, blank=True)
    datepaid = models.DateField(null=True, db_column='datePaid', blank=True) # Field name made lowercase.
    paymentmethod = models.CharField(max_length=100L, db_column='paymentMethod', blank=True) # Field name made lowercase.
    generalcomment = models.TextField(db_column='generalComment', blank=True) # Field name made lowercase.
    contact = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'gospelTripAssignment'

class Gospeltripdestination(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    location = models.CharField(max_length=100L)
    gospeltypeid = models.IntegerField(db_column='gospelTypeID') # Field name made lowercase.
    secondyear = models.IntegerField(db_column='secondYear') # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripDestination'

class Gospeltripdriver(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=200L)
    phone = models.CharField(max_length=200L, blank=True)
    class Meta:
        db_table = 'gospelTripDriver'

class Gospeltripflight(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    outflightnumber = models.CharField(max_length=100L, db_column='outFlightNumber', blank=True) # Field name made lowercase.
    outairline = models.CharField(max_length=100L, db_column='outAirline', blank=True) # Field name made lowercase.
    outdeptairport = models.CharField(max_length=100L, db_column='outDeptAirport', blank=True) # Field name made lowercase.
    outdeptdatetime = models.DateTimeField(null=True, db_column='outDeptDateTime', blank=True) # Field name made lowercase.
    outarrivalairport = models.CharField(max_length=100L, db_column='outArrivalAirport', blank=True) # Field name made lowercase.
    outarrivaldatetime = models.DateTimeField(null=True, db_column='outArrivalDateTime', blank=True) # Field name made lowercase.
    retflightnumber = models.CharField(max_length=100L, db_column='retFlightNumber', blank=True) # Field name made lowercase.
    retairline = models.CharField(max_length=100L, db_column='retAirline', blank=True) # Field name made lowercase.
    retdeptairport = models.CharField(max_length=100L, db_column='retDeptAirport', blank=True) # Field name made lowercase.
    retdeptdatetime = models.DateTimeField(null=True, db_column='retDeptDateTime', blank=True) # Field name made lowercase.
    retarrivalairport = models.CharField(max_length=100L, db_column='retArrivalAirport', blank=True) # Field name made lowercase.
    retarrivaldatetime = models.DateTimeField(null=True, db_column='retArrivalDateTime', blank=True) # Field name made lowercase.
    flightcomment = models.TextField(db_column='flightComment', blank=True) # Field name made lowercase.
    interoutflightnumber = models.CharField(max_length=100L, db_column='interOutFlightNumber', blank=True) # Field name made lowercase.
    interoutairline = models.CharField(max_length=100L, db_column='interOutAirline', blank=True) # Field name made lowercase.
    interoutdeptairport = models.CharField(max_length=100L, db_column='interOutDeptAirport', blank=True) # Field name made lowercase.
    interoutdeptdatetime = models.DateTimeField(null=True, db_column='interOutDeptDateTime', blank=True) # Field name made lowercase.
    interoutarrivalairport = models.CharField(max_length=100L, db_column='interOutArrivalAirport', blank=True) # Field name made lowercase.
    interoutarrivaldatetime = models.DateTimeField(null=True, db_column='interOutArrivalDateTime', blank=True) # Field name made lowercase.
    interretflightnumber = models.CharField(max_length=100L, db_column='interRetFlightNumber', blank=True) # Field name made lowercase.
    interretairline = models.CharField(max_length=100L, db_column='interRetAirline', blank=True) # Field name made lowercase.
    interretdeptairport = models.CharField(max_length=100L, db_column='interRetDeptAirport', blank=True) # Field name made lowercase.
    interretdeptdatetime = models.DateTimeField(null=True, db_column='interRetDeptDateTime', blank=True) # Field name made lowercase.
    interretarrivalairport = models.CharField(max_length=100L, db_column='interRetArrivalAirport', blank=True) # Field name made lowercase.
    interretarrivaldatetime = models.DateTimeField(null=True, db_column='interRetArrivalDateTime', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripFlight'

class Gospeltripinformation(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    fname = models.CharField(max_length=10L)
    mname = models.CharField(max_length=10L, blank=True)
    lname = models.CharField(max_length=20L)
    gospelcitizenshipid = models.CharField(max_length=100L, db_column='gospelCitizenshipID') # Field name made lowercase.
    vehicle = models.CharField(max_length=10L)
    vehicleinsurance = models.CharField(max_length=200L, db_column='vehicleInsurance', blank=True) # Field name made lowercase.
    comments = models.TextField(blank=True)
    allergy = models.TextField(blank=True)
    costcovered = models.CharField(max_length=10L, db_column='costCovered') # Field name made lowercase.
    flightcovered = models.CharField(max_length=10L, db_column='flightCovered') # Field name made lowercase.
    costavailable = models.CharField(max_length=200L, db_column='costAvailable', blank=True) # Field name made lowercase.
    vehicleavailable = models.CharField(max_length=10L, db_column='vehicleAvailable') # Field name made lowercase.
    departingairport = models.CharField(max_length=200L, db_column='departingAirport', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripInformation'

class Gospeltriplanguage(models.Model):
    language = models.CharField(max_length=100L)
    class Meta:
        db_table = 'gospelTripLanguage'

class Gospeltripoverseer(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    name = models.CharField(max_length=200L, blank=True)
    firstname = models.CharField(max_length=200L, db_column='firstName', blank=True) # Field name made lowercase.
    lastname = models.CharField(max_length=200L, db_column='lastName', blank=True) # Field name made lowercase.
    locality = models.CharField(max_length=200L, blank=True)
    gender = models.CharField(max_length=200L, blank=True)
    pref1 = models.CharField(max_length=200L, blank=True)
    preftext1 = models.TextField(db_column='prefText1', blank=True) # Field name made lowercase.
    car1 = models.CharField(max_length=3L, blank=True)
    pref2 = models.CharField(max_length=200L, blank=True)
    preftext2 = models.TextField(db_column='prefText2', blank=True) # Field name made lowercase.
    car2 = models.CharField(max_length=3L, blank=True)
    pref3 = models.CharField(max_length=200L, blank=True)
    preftext3 = models.TextField(db_column='prefText3', blank=True) # Field name made lowercase.
    car3 = models.CharField(max_length=3L, blank=True)
    pref4 = models.CharField(max_length=200L, blank=True)
    preftext4 = models.TextField(db_column='prefText4', blank=True) # Field name made lowercase.
    car4 = models.CharField(max_length=3L, blank=True)
    pref5 = models.CharField(max_length=200L, blank=True)
    preftext5 = models.TextField(db_column='prefText5', blank=True) # Field name made lowercase.
    car5 = models.CharField(max_length=3L, blank=True)
    pref6 = models.CharField(max_length=200L, blank=True)
    preftext6 = models.TextField(db_column='prefText6', blank=True) # Field name made lowercase.
    car6 = models.CharField(max_length=3L, blank=True)
    lang1 = models.CharField(max_length=200L, blank=True)
    prof1 = models.CharField(max_length=200L, blank=True)
    langtext1 = models.TextField(db_column='langText1', blank=True) # Field name made lowercase.
    lang2 = models.CharField(max_length=200L, blank=True)
    prof2 = models.CharField(max_length=200L, blank=True)
    langtext2 = models.TextField(db_column='langText2', blank=True) # Field name made lowercase.
    lang3 = models.CharField(max_length=200L, blank=True)
    prof3 = models.CharField(max_length=200L, blank=True)
    langtext3 = models.TextField(db_column='langText3', blank=True) # Field name made lowercase.
    lang4 = models.CharField(max_length=200L, blank=True)
    prof4 = models.CharField(max_length=200L, blank=True)
    langtext4 = models.TextField(db_column='langText4', blank=True) # Field name made lowercase.
    lang5 = models.CharField(max_length=200L, blank=True)
    prof5 = models.CharField(max_length=200L, blank=True)
    langtext5 = models.TextField(db_column='langText5', blank=True) # Field name made lowercase.
    lang6 = models.CharField(max_length=200L, blank=True)
    prof6 = models.CharField(max_length=200L, blank=True)
    langtext6 = models.TextField(db_column='langText6', blank=True) # Field name made lowercase.
    contact = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'gospelTripOverseer'

class Gospeltrippassport(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    fname = models.CharField(max_length=100L, blank=True)
    mname = models.CharField(max_length=100L, blank=True)
    lname = models.CharField(max_length=100L, blank=True)
    citizenship = models.CharField(max_length=100L, blank=True)
    gospelcitizenshipid = models.CharField(max_length=50L, db_column='gospelCitizenshipID') # Field name made lowercase.
    gospelcitizenshipother = models.CharField(max_length=50L, db_column='gospelCitizenshipOther', blank=True) # Field name made lowercase.
    expirationdate = models.DateField(null=True, db_column='expirationDate', blank=True) # Field name made lowercase.
    passportnumber = models.CharField(max_length=100L, db_column='passportNumber', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripPassport'

class Gospeltrippayment(models.Model):
    payment = models.CharField(max_length=100L)
    class Meta:
        db_table = 'gospelTripPayment'

class Gospeltripproficiency(models.Model):
    proficiency = models.CharField(max_length=100L)
    class Meta:
        db_table = 'gospelTripProficiency'

class Gospeltriprun(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=200L)
    time = models.DateTimeField(null=True, blank=True)
    startloc = models.CharField(max_length=200L, db_column='startLoc', blank=True) # Field name made lowercase.
    endloc = models.CharField(max_length=200L, db_column='endLoc', blank=True) # Field name made lowercase.
    gospeltripvehicleid = models.ForeignKey('Gospeltripvehicle', null=True, db_column='gospelTripVehicleID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripRun'

class Gospeltriprundriver(models.Model):
    gospeltriprunid = models.ForeignKey(Gospeltriprun, db_column='gospelTripRunID') # Field name made lowercase.
    gospeltripdriverid = models.ForeignKey(Gospeltripdriver, db_column='gospelTripDriverID') # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripRunDriver'

class Gospeltripselection(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    gospeltypeid = models.IntegerField(db_column='gospelTypeID') # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripSelection'

class Gospeltripvehicle(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    vehiclename = models.CharField(max_length=100L, db_column='vehicleName') # Field name made lowercase.
    numpassenger = models.IntegerField(null=True, db_column='numPassenger', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'gospelTripVehicle'

class Gospeltype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    type = models.CharField(max_length=100L)
    class Meta:
        db_table = 'gospelType'

class Gp(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    active = models.IntegerField(db_column='Active') # Field name made lowercase.
    gpid = models.IntegerField(db_column='gpID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    termname = models.CharField(max_length=45L, db_column='termName') # Field name made lowercase.
    class Meta:
        db_table = 'gp'

class Gpstats(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    gpid = models.IntegerField(db_column='gpID') # Field name made lowercase.
    week = models.IntegerField()
    gptypeid = models.IntegerField(db_column='gpTypeID') # Field name made lowercase.
    value = models.IntegerField()
    teamid = models.IntegerField(db_column='teamID') # Field name made lowercase.
    termname = models.CharField(max_length=45L, db_column='termName') # Field name made lowercase.
    class Meta:
        db_table = 'gpStats'

class Gpteam(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    gpid = models.IntegerField(db_column='gpID') # Field name made lowercase.
    teamid = models.IntegerField(db_column='teamID') # Field name made lowercase.
    class Meta:
        db_table = 'gpTeam'

class Gptype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    statname = models.CharField(max_length=26L, db_column='statName') # Field name made lowercase.
    class Meta:
        db_table = 'gpType'

class GradActivity(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=32L, unique=True)
    description = models.TextField()
    class Meta:
        db_table = 'grad_activity'

class GradAdmin(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    gradactivityid = models.IntegerField(db_column='gradActivityID') # Field name made lowercase.
    showactivity = models.IntegerField(db_column='showActivity') # Field name made lowercase.
    duedate = models.DateField(null=True, db_column='dueDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'grad_admin'

class GradConsiderations(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    attend = models.CharField(max_length=4L, blank=True)
    fellowship = models.CharField(max_length=3L, blank=True)
    finance = models.CharField(max_length=4L, blank=True)
    plans = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = 'grad_considerations'

class GradInvites(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    num_invites = models.IntegerField(null=True, blank=True)
    num_dvd = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'grad_invites'

class GradRemembrance(models.Model):
    traineeid = models.IntegerField(primary_key=True, db_column='traineeID') # Field name made lowercase.
    remembrance1 = models.TextField(blank=True)
    remembrance2 = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    localityid = models.IntegerField(null=True, db_column='localityID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'grad_remembrance'

class GradSpeaking(models.Model):
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    speaking = models.TextField()
    class Meta:
        db_table = 'grad_speaking'

class GradStats(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    num_invites = models.IntegerField()
    burden1 = models.IntegerField(null=True, blank=True)
    burden2 = models.IntegerField(null=True, blank=True)
    burden3 = models.IntegerField(null=True, blank=True)
    pref1 = models.IntegerField(null=True, blank=True)
    pref2 = models.IntegerField(null=True, blank=True)
    pref3 = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=255L, blank=True)
    email = models.CharField(max_length=255L, blank=True)
    phone = models.CharField(max_length=255L, blank=True)
    q1 = models.IntegerField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.IntegerField()
    plans = models.TextField()
    class Meta:
        db_table = 'grad_stats'

class GradSurvey(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    outlinesections = models.IntegerField(db_column='outlineSections') # Field name made lowercase.
    outline = models.TextField()
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    class Meta:
        db_table = 'grad_survey'

class GradTestimony(models.Model):
    id = models.IntegerField(primary_key=True)
    traineeid = models.IntegerField(null=True, db_column='traineeID', blank=True) # Field name made lowercase.
    termid = models.IntegerField(null=True, db_column='termID', blank=True) # Field name made lowercase.
    testimony = models.TextField(blank=True)
    fellowship = models.TextField(blank=True)
    question3 = models.TextField(blank=True)
    question4 = models.TextField(blank=True)
    testimony_speak = models.IntegerField(null=True, blank=True)
    fellowship_speak = models.IntegerField(null=True, blank=True)
    mod_date = models.DateTimeField()
    class Meta:
        db_table = 'grad_testimony'

class Greekparsing(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField()
    class Meta:
        db_table = 'greekParsing'

class Greekuserstats(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    greekvocabid = models.IntegerField(db_column='greekVocabID') # Field name made lowercase.
    numtimes = models.IntegerField(db_column='numTimes') # Field name made lowercase.
    correct = models.IntegerField()
    class Meta:
        db_table = 'greekUserStats'

class Greekvocab(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    greek = models.CharField(max_length=50L)
    english = models.CharField(max_length=50L)
    chapter = models.IntegerField(null=True, blank=True)
    parsingid = models.IntegerField(null=True, db_column='parsingID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'greekVocab'

class Gtcasurvey(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    name = models.TextField()
    term = models.IntegerField()
    college = models.TextField()
    major = models.TextField()
    locality = models.TextField()
    charlottesville = models.CharField(max_length=5L)
    fortcollins = models.CharField(max_length=5L, db_column='fortCollins') # Field name made lowercase.
    madison = models.CharField(max_length=5L)
    philadelphia = models.CharField(max_length=5L)
    montreal = models.CharField(max_length=5L)
    capacity = models.TextField()
    length = models.TextField(blank=True)
    released = models.CharField(max_length=20L, blank=True)
    fellowship = models.CharField(max_length=3L, blank=True)
    joinmonth = models.IntegerField(db_column='joinMonth') # Field name made lowercase.
    joinyear = models.IntegerField(db_column='joinYear') # Field name made lowercase.
    notes = models.TextField(blank=True)
    class Meta:
        db_table = 'gtcaSurvey'

class Hcsurvey(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    residenceid = models.IntegerField(db_column='ResidenceID') # Field name made lowercase.
    hcuserid = models.IntegerField(db_column='HCUserID') # Field name made lowercase.
    periodid = models.IntegerField(null=True, db_column='periodID', blank=True) # Field name made lowercase.
    atmosphere = models.TextField()
    situations = models.TextField()
    comments = models.TextField()
    class Meta:
        db_table = 'hcSurvey'

class Hcsurveytraineenotes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    hcsurveyid = models.IntegerField(db_column='hcSurveyID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    comments = models.TextField()
    class Meta:
        db_table = 'hcSurveyTraineeNotes'

class Hcrecmdqs(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    residenceid = models.IntegerField(db_column='ResidenceID') # Field name made lowercase.
    hcuserid = models.IntegerField(db_column='HCUserID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    atmosphere = models.TextField()
    situations = models.TextField()
    comments = models.TextField()
    class Meta:
        db_table = 'hcrecmdqs'

class Houseinspectionfaq(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    question = models.TextField()
    answer = models.TextField()
    useful = models.IntegerField()
    tag = models.CharField(max_length=14L)
    askerid = models.IntegerField(db_column='askerID') # Field name made lowercase.
    class Meta:
        db_table = 'houseInspectionFAQ'

class Importsql(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    transactionid = models.IntegerField(db_column='transactionID') # Field name made lowercase.
    sqlstatement = models.TextField(db_column='sqlStatement') # Field name made lowercase.
    undostatement = models.TextField(db_column='undoStatement', blank=True) # Field name made lowercase.
    iscompleted = models.IntegerField(db_column='isCompleted') # Field name made lowercase.
    class Meta:
        db_table = 'importSQL'

class Importsqlauthor(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    transactionid = models.IntegerField(db_column='transactionID') # Field name made lowercase.
    timebegin = models.DateTimeField(null=True, db_column='timeBegin', blank=True) # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    isfinished = models.IntegerField(null=True, db_column='isFinished', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'importSQLAuthor'

class ImportTrainee(models.Model):
    firstname = models.TextField(db_column='firstName', blank=True) # Field name made lowercase.
    nickname = models.TextField(db_column='nickName', blank=True) # Field name made lowercase.
    lastname = models.TextField(db_column='lastName', blank=True) # Field name made lowercase.
    middleinitial = models.TextField(db_column='middleInitial', blank=True) # Field name made lowercase.
    maidenname = models.TextField(db_column='maidenName', blank=True) # Field name made lowercase.
    birthdate = models.TextField(db_column='birthDate', blank=True) # Field name made lowercase.
    gender = models.TextField(blank=True)
    address = models.TextField(blank=True)
    city = models.TextField(blank=True)
    state = models.TextField(blank=True)
    zip = models.TextField(blank=True)
    country = models.TextField(blank=True)
    maritalstatus = models.TextField(db_column='maritalStatus', blank=True) # Field name made lowercase.
    phonenumber = models.TextField(db_column='phoneNumber', blank=True) # Field name made lowercase.
    cellnumber = models.TextField(db_column='cellNumber', blank=True) # Field name made lowercase.
    email = models.TextField(blank=True)
    sendinglocality = models.TextField(db_column='sendingLocality', blank=True) # Field name made lowercase.
    datebegin = models.TextField(db_column='dateBegin', blank=True) # Field name made lowercase.
    termscompleted = models.TextField(db_column='termsCompleted', blank=True) # Field name made lowercase.
    couple = models.TextField(blank=True)
    emergencycontact = models.TextField(db_column='emergencyContact', blank=True) # Field name made lowercase.
    emergencyaddress = models.TextField(db_column='emergencyAddress', blank=True) # Field name made lowercase.
    emergencyphone = models.TextField(db_column='emergencyPhone', blank=True) # Field name made lowercase.
    emergencyphone2 = models.TextField(db_column='emergencyPhone2', blank=True) # Field name made lowercase.
    readot = models.TextField(db_column='readOT', blank=True) # Field name made lowercase.
    readnt = models.TextField(db_column='readNT', blank=True) # Field name made lowercase.
    ta = models.TextField(db_column='TA', blank=True) # Field name made lowercase.
    mentor = models.TextField(blank=True)
    college = models.TextField(blank=True)
    major = models.TextField(blank=True)
    degree = models.TextField(blank=True)
    gospelpref1 = models.TextField(db_column='gospelPref1', blank=True) # Field name made lowercase.
    gospelpref2 = models.TextField(db_column='gospelPref2', blank=True) # Field name made lowercase.
    vehicleinfo = models.TextField(db_column='vehicleInfo', blank=True) # Field name made lowercase.
    vehiclelicense = models.TextField(db_column='vehicleLicense', blank=True) # Field name made lowercase.
    vehiclecolor = models.TextField(db_column='vehicleColor', blank=True) # Field name made lowercase.
    vehiclecapacity = models.TextField(db_column='vehicleCapacity', blank=True) # Field name made lowercase.
    residenceid = models.TextField(db_column='residenceID', blank=True) # Field name made lowercase.
    officeid = models.TextField(db_column='officeID', blank=True) # Field name made lowercase.
    stpt = models.TextField(db_column='STPT', blank=True) # Field name made lowercase.
    stft = models.TextField(db_column='STFT', blank=True) # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True) # Field name made lowercase.
    traineeid = models.IntegerField(null=True, db_column='traineeID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'import_trainee'

class Inspectionscore(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    inspectoruserid = models.IntegerField(null=True, db_column='inspectorUserID', blank=True) # Field name made lowercase.
    residenceid = models.IntegerField(db_column='residenceID') # Field name made lowercase.
    score = models.FloatField(null=True, blank=True)
    ricuserid = models.IntegerField(null=True, db_column='RICUserID', blank=True) # Field name made lowercase.
    date = models.DateField()
    note = models.TextField(blank=True)
    uninspectable = models.IntegerField()
    class Meta:
        db_table = 'inspectionScore'

class Interimcalendar(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    startdate = models.DateField(db_column='startDate') # Field name made lowercase.
    enddate = models.DateField(db_column='endDate') # Field name made lowercase.
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'interimCalendar'

class Interimexit(models.Model):
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    interimintentionid = models.IntegerField(db_column='interimIntentionID') # Field name made lowercase.
    unsure = models.CharField(max_length=3L)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = 'interimExit'

class Interimintention(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField()
    placeholder = models.TextField(db_column='placeHolder', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'interimIntention'

class Leaveslip(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userID') # Field name made lowercase.
    leaveslipcategoryid = models.ForeignKey('Leaveslipcategory', db_column='leaveSlipCategoryID') # Field name made lowercase.
    submissiondatetime = models.DateTimeField(db_column='submissionDateTime') # Field name made lowercase.
    remarks = models.TextField(blank=True)
    requiresfellowship = models.IntegerField(db_column='requiresFellowship') # Field name made lowercase.
    assignedtaid = models.IntegerField(null=True, db_column='assignedTAID', blank=True) # Field name made lowercase.
    informeduserid = models.IntegerField(null=True, db_column='informedUserID', blank=True) # Field name made lowercase.
    taremarks = models.TextField(db_column='TARemarks', blank=True) # Field name made lowercase.
    taprivateremarks = models.TextField(db_column='TAPrivateRemarks', blank=True) # Field name made lowercase.
    haspaperleaveslip = models.IntegerField(null=True, db_column='hasPaperLeaveSlip', blank=True) # Field name made lowercase.
    svscheduleinstanceid = models.ForeignKey('Svscheduleinstance', null=True, db_column='svScheduleInstanceID', blank=True) # Field name made lowercase.
    svserviceid = models.IntegerField(null=True, db_column='svServiceID', blank=True) # Field name made lowercase.
    sistertaapproval = models.CharField(max_length=1L, db_column='sisterTAApproval', blank=True) # Field name made lowercase.
    didnotinform = models.IntegerField(db_column='didNotInform') # Field name made lowercase.
    texted = models.IntegerField()
    class Meta:
        db_table = 'leaveSlip'

class Leaveslipapproval(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    leaveslipid = models.ForeignKey(Leaveslip, unique=True, db_column='leaveSlipID') # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userID') # Field name made lowercase.
    approvaldatetime = models.DateTimeField(db_column='approvalDateTime') # Field name made lowercase.
    approvalstatus = models.CharField(max_length=1L, db_column='approvalStatus') # Field name made lowercase.
    remarks = models.TextField(blank=True)
    affectsperfectattendance = models.IntegerField(db_column='affectsPerfectAttendance') # Field name made lowercase.
    class Meta:
        db_table = 'leaveSlipApproval'

class Leaveslipcategory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    leavesliptypeid = models.ForeignKey('Leavesliptype', db_column='leaveSlipTypeID') # Field name made lowercase.
    affectsperfectattendance = models.IntegerField(db_column='affectsPerfectAttendance') # Field name made lowercase.
    special = models.IntegerField()
    class Meta:
        db_table = 'leaveSlipCategory'

class Leaveslipevent(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    leaveslipid = models.ForeignKey(Leaveslip, db_column='leaveSlipID') # Field name made lowercase.
    scheduleeventid = models.ForeignKey('Scheduleevent', db_column='scheduleEventID') # Field name made lowercase.
    date = models.DateField()
    class Meta:
        db_table = 'leaveSlipEvent'

class Leaveslipmealout(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    leaveslipid = models.IntegerField(db_column='leaveSlipID') # Field name made lowercase.
    name = models.CharField(max_length=64L, blank=True)
    location = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'leaveSlipMealOut'

class Leaveslipmember(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    leaveslipid = models.ForeignKey(Leaveslip, db_column='leaveSlipID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    class Meta:
        db_table = 'leaveSlipMember'

class Leaveslipnightout(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    leaveslipid = models.IntegerField(db_column='leaveSlipID') # Field name made lowercase.
    name = models.CharField(max_length=64L, blank=True)
    phone = models.CharField(max_length=14L, blank=True)
    address = models.CharField(max_length=255L, blank=True)
    hcname = models.CharField(max_length=30L, db_column='HCname', blank=True) # Field name made lowercase.
    verifyhc = models.IntegerField(null=True, db_column='verifyHC', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'leaveSlipNightOut'

class Leaveslipstatus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    description = models.TextField()
    statuscode = models.CharField(max_length=2L, unique=True, db_column='statusCode') # Field name made lowercase.
    class Meta:
        db_table = 'leaveSlipStatus'

class Leaveslipta(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    leaveslipid = models.IntegerField(null=True, db_column='leaveSlipID', blank=True) # Field name made lowercase.
    trainingassistantid = models.IntegerField(null=True, db_column='trainingAssistantID', blank=True) # Field name made lowercase.
    date_assigned = models.DateTimeField()
    class Meta:
        db_table = 'leaveSlipTA'

class Leavesliptype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'leaveSlipType'

class Leaveslipgroupview(models.Model):
    scheduleeventid = models.IntegerField(db_column='scheduleEventID') # Field name made lowercase.
    leaveslipid = models.IntegerField(db_column='leaveSlipID') # Field name made lowercase.
    leaveslipcategoryid = models.IntegerField(db_column='leaveSlipCategoryID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    date = models.DateField()
    class Meta:
        db_table = 'leaveslipgroupview'

class LeaveslipinfoGroup(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    leaveslipid = models.IntegerField(db_column='leaveSlipID') # Field name made lowercase.
    date = models.DateField()
    starttime = models.DateTimeField(db_column='startTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime') # Field name made lowercase.
    class Meta:
        db_table = 'leaveslipinfo_group'

class Leaveslippersonalview(models.Model):
    scheduleeventid = models.IntegerField(db_column='scheduleEventID') # Field name made lowercase.
    leaveslipid = models.IntegerField(db_column='leaveSlipID') # Field name made lowercase.
    leaveslipcategoryid = models.IntegerField(db_column='leaveSlipCategoryID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    date = models.DateField()
    class Meta:
        db_table = 'leaveslippersonalview'

class LinensRequests(models.Model):
    id = models.IntegerField(primary_key=True)
    residence_id = models.IntegerField()
    trainee_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    active = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()
    completed = models.IntegerField()
    completed_date = models.DateField()
    priority = models.IntegerField()
    class Meta:
        db_table = 'linens_requests'

class LinensTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=100L)
    class Meta:
        db_table = 'linens_types'

class Locality(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    city = models.CharField(max_length=255L, unique=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    mrtype = models.IntegerField(db_column='MRType') # Field name made lowercase.
    class Meta:
        db_table = 'locality'

class Logbrowser(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField()
    class Meta:
        db_table = 'logBrowser'

class Logclasslogin(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    time = models.DateTimeField()
    ipaddress = models.CharField(max_length=15L, db_column='ipAddress') # Field name made lowercase.
    session = models.CharField(max_length=32L, blank=True)
    class Meta:
        db_table = 'logClassLogin'

class Loglogin(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    username = models.CharField(max_length=32L)
    status = models.CharField(max_length=7L)
    time = models.DateTimeField()
    ipaddr = models.IntegerField(null=True, db_column='ipAddr', blank=True) # Field name made lowercase.
    session = models.CharField(max_length=32L, blank=True)
    class Meta:
        db_table = 'logLogin'

class Lognightlytasks(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=32L)
    timestamp = models.DateTimeField()
    messages = models.TextField(blank=True)
    class Meta:
        db_table = 'logNightlyTasks'

class Logpage(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(null=True, db_column='userID', blank=True) # Field name made lowercase.
    pageid = models.IntegerField(null=True, db_column='pageID', blank=True) # Field name made lowercase.
    pageurl = models.TextField(db_column='pageUrl', blank=True) # Field name made lowercase.
    browserid = models.IntegerField(null=True, db_column='browserID', blank=True) # Field name made lowercase.
    postparam = models.TextField(db_column='postParam', blank=True) # Field name made lowercase.
    getparam = models.TextField(db_column='getParam', blank=True) # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime') # Field name made lowercase.
    endtime = models.DateTimeField(null=True, db_column='endTime', blank=True) # Field name made lowercase.
    loadtime = models.FloatField(null=True, db_column='loadTime', blank=True) # Field name made lowercase.
    session = models.CharField(max_length=32L, blank=True)
    class Meta:
        db_table = 'logPage'

class Lookup(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField(blank=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = 'lookup'

class Lsbook(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=32L, blank=True)
    nickname = models.CharField(max_length=8L, blank=True)
    nummessages = models.IntegerField(null=True, db_column='numMessages', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'lsBook'

class Lsoffense(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    lsoffensereasonid = models.IntegerField(db_column='lsOffenseReasonID') # Field name made lowercase.
    active = models.IntegerField()
    creationdate = models.DateTimeField(db_column='creationDate') # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='lastUpdateDate') # Field name made lowercase.
    iscurrentlymondayoffense = models.IntegerField(db_column='isCurrentlyMondayOffense') # Field name made lowercase.
    numlsowed = models.IntegerField(db_column='numLSOwed') # Field name made lowercase.
    numlsreceived = models.IntegerField(db_column='numLSReceived') # Field name made lowercase.
    signedin = models.CharField(max_length=1L, db_column='signedIn', blank=True) # Field name made lowercase.
    manualhandling = models.IntegerField(db_column='manualHandling') # Field name made lowercase.
    comments = models.CharField(max_length=255L, blank=True)
    tacomments = models.CharField(max_length=255L, db_column='taComments', blank=True) # Field name made lowercase.
    numlsunapplied = models.IntegerField(null=True, db_column='numLSUnapplied', blank=True) # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    class Meta:
        db_table = 'lsOffense'

class Lsoffensereason(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    offensereason = models.CharField(max_length=30L, db_column='offenseReason') # Field name made lowercase.
    ismondayoffense = models.IntegerField(null=True, db_column='isMondayOffense', blank=True) # Field name made lowercase.
    numls = models.IntegerField(null=True, db_column='numLS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'lsOffenseReason'

class Lssubmission(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    lsoffenseid = models.IntegerField(null=True, db_column='lsOffenseID', blank=True) # Field name made lowercase.
    lsbookid = models.IntegerField(null=True, db_column='lsBookID', blank=True) # Field name made lowercase.
    messagenumber = models.IntegerField(null=True, db_column='messageNumber', blank=True) # Field name made lowercase.
    submissiondate = models.DateTimeField(db_column='submissionDate') # Field name made lowercase.
    text = models.TextField()
    finalized = models.IntegerField()
    approved = models.IntegerField()
    class Meta:
        db_table = 'lsSubmission'

class MaintenanceRequests(models.Model):
    id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()
    description = models.TextField()
    residence_id = models.IntegerField()
    room_id = models.IntegerField()
    other_room = models.TextField()
    created_at = models.DateTimeField()
    trainee_id = models.IntegerField()
    active = models.IntegerField()
    completed = models.IntegerField()
    completed_date = models.DateField()
    notes = models.TextField()
    priority = models.IntegerField()
    class Meta:
        db_table = 'maintenance_requests'

class MaintenanceTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100L)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'maintenance_types'

class Mealseatlocation(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=9L)
    class Meta:
        db_table = 'mealSeatLocation'

class Mealseating(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    gender = models.CharField(max_length=1L)
    name = models.CharField(max_length=5L)
    numberoccupied = models.IntegerField(db_column='numberOccupied') # Field name made lowercase.
    capacity = models.IntegerField()
    maxcapacity = models.IntegerField(db_column='maxCapacity') # Field name made lowercase.
    mealseatlocationid = models.IntegerField(db_column='mealSeatLocationID') # Field name made lowercase.
    class Meta:
        db_table = 'mealSeating'

class Newapplications(models.Model):
    applicationid = models.IntegerField(primary_key=True, db_column='applicationID') # Field name made lowercase.
    datetime = models.DateTimeField()
    timestamp = models.DateTimeField()
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    fname = models.CharField(max_length=100L, blank=True)
    mname = models.CharField(max_length=50L, blank=True)
    lname = models.TextField(blank=True)
    gender = models.TextField(blank=True)
    locality = models.TextField(blank=True)
    address = models.TextField(blank=True)
    city = models.TextField(blank=True)
    state = models.TextField(blank=True)
    zip = models.TextField(blank=True)
    country = models.TextField(blank=True)
    phone_home = models.TextField(blank=True)
    phone_cell = models.TextField(blank=True)
    phone_international_home = models.TextField(blank=True)
    phone_international_cell = models.TextField(blank=True)
    birth_date = models.TextField(blank=True)
    citizenship = models.TextField(blank=True)
    automobile = models.TextField(blank=True)
    automobile_seats = models.TextField(blank=True)
    lang_chinese = models.TextField(blank=True)
    lang_spanish = models.TextField(blank=True)
    lang_korean = models.TextField(blank=True)
    otherlang = models.TextField(blank=True)
    college = models.TextField(blank=True)
    major = models.TextField(blank=True)
    degree = models.TextField(blank=True)
    college2 = models.TextField(blank=True)
    major2 = models.TextField(blank=True)
    degree2 = models.TextField(blank=True)
    occupation = models.TextField(blank=True)
    full_time_date = models.TextField(blank=True)
    datesaved = models.TextField(blank=True)
    datebaptized = models.TextField(blank=True)
    churchdate = models.TextField(blank=True)
    firstcontact = models.TextField(blank=True)
    serviceareas = models.TextField(blank=True)
    previoustraining = models.TextField(blank=True)
    read_ot = models.TextField(blank=True)
    read_nt = models.TextField(blank=True)
    maritalstatus = models.TextField(blank=True)
    spousename = models.TextField(blank=True)
    dateofmarriage = models.TextField(blank=True)
    spouseoccupation = models.TextField(blank=True)
    spouseage = models.TextField(blank=True)
    spouseattitude = models.TextField(blank=True)
    dependent = models.TextField(blank=True)
    support_yourself = models.TextField(blank=True)
    support_church = models.TextField(blank=True)
    support_family = models.TextField(blank=True)
    support_other = models.TextField(blank=True)
    support_other_value = models.TextField(blank=True)
    pertinantinformation = models.TextField(blank=True)
    med1 = models.TextField(blank=True)
    med2 = models.TextField(blank=True)
    med2list = models.TextField(blank=True)
    med3 = models.TextField(blank=True)
    med3list = models.TextField(blank=True)
    med4 = models.TextField(blank=True)
    med4_1 = models.TextField(blank=True)
    med4_2 = models.TextField(blank=True)
    med4_3 = models.TextField(blank=True)
    med4_4 = models.TextField(blank=True)
    med4_5 = models.TextField(blank=True)
    med4_6 = models.TextField(blank=True)
    med4_7 = models.TextField(blank=True)
    med4_8 = models.TextField(blank=True)
    med4list = models.TextField(blank=True)
    med5 = models.TextField(blank=True)
    med6 = models.TextField(blank=True)
    med7 = models.TextField(blank=True)
    med8 = models.TextField(blank=True)
    med9_1 = models.TextField(blank=True)
    med9_2 = models.TextField(blank=True)
    med9_3 = models.TextField(blank=True)
    med9_4 = models.TextField(blank=True)
    med9_5 = models.TextField(blank=True)
    med9_6 = models.TextField(blank=True)
    med9_7 = models.TextField(blank=True)
    med9_8 = models.TextField(blank=True)
    med9_9 = models.TextField(blank=True)
    med9_10 = models.TextField(blank=True)
    med10 = models.TextField(blank=True)
    med11 = models.TextField(blank=True)
    med12 = models.TextField(blank=True)
    med13 = models.TextField(blank=True)
    med14 = models.TextField(blank=True)
    med15 = models.TextField(blank=True)
    med16 = models.TextField(blank=True)
    tobacco = models.TextField(blank=True)
    med17_1 = models.TextField(blank=True)
    alcohol = models.TextField(blank=True)
    med17_2 = models.TextField(blank=True)
    drugs = models.TextField(blank=True)
    med17_3 = models.TextField(blank=True)
    exam = models.TextField(blank=True)
    med18 = models.TextField(blank=True)
    xray = models.TextField(blank=True)
    med19 = models.TextField(blank=True)
    med20 = models.TextField(blank=True)
    med21 = models.TextField(blank=True)
    med22 = models.TextField(blank=True)
    med23_1 = models.TextField(blank=True)
    med23_2 = models.TextField(blank=True)
    med24 = models.TextField(blank=True)
    med25 = models.TextField(blank=True)
    td_test = models.TextField(blank=True)
    hepatitisa1 = models.TextField(blank=True)
    hepatitisa2 = models.TextField(blank=True)
    hepatitisb1 = models.TextField(blank=True)
    hepatitisb2 = models.TextField(blank=True)
    hepatitisb3 = models.TextField(blank=True)
    tbdate = models.TextField(blank=True)
    tbresult = models.TextField(blank=True)
    xraydate = models.TextField(blank=True)
    cxrayresult = models.TextField(blank=True)
    mmr1 = models.TextField(blank=True)
    mmr2 = models.TextField(blank=True)
    immunizations = models.TextField(blank=True)
    height = models.TextField(blank=True)
    weight = models.TextField(blank=True)
    med28 = models.TextField(blank=True)
    med28_1 = models.TextField(blank=True)
    med30 = models.TextField(blank=True)
    emergencyname = models.TextField(blank=True)
    emergencyaddress = models.TextField(blank=True)
    emergencytelephone = models.TextField(blank=True)
    emergencyemail = models.TextField(blank=True)
    insurance = models.TextField(blank=True)
    health_concerns = models.TextField(blank=True)
    status = models.CharField(max_length=1L)
    testimony = models.TextField(blank=True)
    poor_english = models.TextField(blank=True)
    gospelpref1 = models.TextField(blank=True)
    gospelpref2 = models.TextField(blank=True)
    aka = models.CharField(max_length=100L, blank=True)
    audio_video = models.TextField(blank=True)
    auto_mechanics = models.TextField(blank=True)
    automobile_color = models.TextField(blank=True)
    automobile_license = models.TextField(blank=True)
    automobile_model = models.TextField(blank=True)
    bachelors = models.TextField(blank=True)
    carpentry = models.TextField(blank=True)
    citizen = models.TextField(blank=True)
    comp_database = models.TextField(blank=True)
    comp_hardware = models.TextField(blank=True)
    comp_networking = models.TextField(blank=True)
    comp_programming = models.TextField(blank=True)
    electrical = models.TextField(blank=True)
    emergencytelephone2 = models.TextField(blank=True)
    facility_maint = models.TextField(blank=True)
    floor_covering = models.TextField(blank=True)
    gardening = models.TextField(blank=True)
    graphic_design = models.TextField(blank=True)
    landscaping = models.TextField(blank=True)
    language_or_char = models.TextField(blank=True)
    locality_country = models.TextField(blank=True)
    locality_state = models.TextField(blank=True)
    locality_other = models.TextField(blank=True)
    locality_other_country = models.TextField(blank=True)
    maidenname = models.TextField(blank=True)
    medical_training = models.TextField(blank=True)
    photography = models.TextField(blank=True)
    picture_framing = models.TextField(blank=True)
    plumbing = models.TextField(blank=True)
    prof_writing = models.TextField(blank=True)
    security_safety = models.TextField(blank=True)
    sewing = models.TextField(blank=True)
    skills_other = models.TextField(blank=True)
    terms = models.TextField(blank=True)
    web_programming = models.TextField(blank=True)
    med6a = models.TextField(blank=True)
    elder_recommendation = models.TextField(blank=True)
    elder_participation = models.CharField(max_length=1L, blank=True)
    elder_knowledge = models.CharField(max_length=1L, blank=True)
    elder_work_together = models.CharField(max_length=1L, blank=True)
    elder_work_ethic = models.CharField(max_length=1L, blank=True)
    elder_in_relationship = models.CharField(max_length=3L, blank=True)
    elder_relationship_explain = models.TextField(blank=True)
    elder_understand_relationship_restriction = models.CharField(max_length=3L, blank=True)
    elder_understand_possible_dismissal = models.CharField(max_length=3L, blank=True)
    elder_abide_relationship_restriction = models.CharField(max_length=3L, blank=True)
    elder_understand_english = models.CharField(max_length=3L, blank=True)
    elder_recommend = models.CharField(max_length=16L, blank=True)
    elder_shepherd = models.CharField(max_length=64L, blank=True)
    elder_shepherd_cell = models.CharField(max_length=32L, blank=True)
    elder_shepherd_email = models.CharField(max_length=64L, blank=True)
    elder_elderfname = models.TextField(blank=True)
    elder_elderlname = models.TextField(blank=True)
    elder_elderemail = models.TextField(blank=True)
    elder_eldercell = models.TextField(blank=True)
    elder_paper_recommendation = models.CharField(max_length=1L, blank=True)
    deleted = models.CharField(max_length=1L, blank=True)
    raisedinchurch = models.TextField(blank=True)
    attend_two_years = models.TextField(blank=True)
    attend_explain = models.TextField(blank=True)
    college_grad_date = models.TextField(blank=True)
    skype = models.TextField(blank=True)
    college_country = models.TextField(blank=True)
    college2_country = models.IntegerField(null=True, blank=True)
    previoustraining2 = models.IntegerField(null=True, blank=True)
    suffix = models.CharField(max_length=50L, blank=True)
    twitter = models.TextField(blank=True)
    lang_mandarin = models.TextField(blank=True)
    lang_cantonese = models.TextField(blank=True)
    spouse_attending = models.TextField(blank=True)
    spouse_plans = models.TextField(blank=True)
    previoustrainingdate = models.TextField(blank=True)
    medapproval = models.CharField(max_length=18L, blank=True)
    approval = models.CharField(max_length=13L, blank=True)
    consecration = models.CharField(max_length=15L, blank=True)
    med_comments = models.TextField(blank=True)
    internationalforms = models.CharField(max_length=84L, db_column='internationalForms', blank=True) # Field name made lowercase.
    overseer_comments = models.TextField(blank=True)
    international_comments = models.TextField(blank=True)
    elder_erec_complete = models.CharField(max_length=3L, db_column='elder_eRec_complete', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'newApplications'

class Newapplicationsstatus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    newapplicationsid = models.IntegerField(db_column='newApplicationsID') # Field name made lowercase.
    approveddennis = models.CharField(max_length=3L, db_column='approvedDennis') # Field name made lowercase.
    approvedandrew = models.CharField(max_length=3L, db_column='approvedAndrew') # Field name made lowercase.
    approvedmedical = models.CharField(max_length=3L, db_column='approvedMedical') # Field name made lowercase.
    provisionalmedical = models.CharField(max_length=3L, db_column='provisionalMedical') # Field name made lowercase.
    approvedoverall = models.CharField(max_length=3L, db_column='approvedOverall') # Field name made lowercase.
    provisionalacceptance = models.CharField(max_length=3L, db_column='provisionalAcceptance') # Field name made lowercase.
    sentacknowledgement = models.CharField(max_length=3L, db_column='sentAcknowledgement') # Field name made lowercase.
    sentacceptance = models.CharField(max_length=3L, db_column='sentAcceptance') # Field name made lowercase.
    timestampsentacknowledgement = models.DateTimeField(db_column='timestampSentAcknowledgement') # Field name made lowercase.
    sentinsurance = models.CharField(max_length=3L, db_column='sentInsurance') # Field name made lowercase.
    sentwebsiteinfo = models.CharField(max_length=3L, db_column='sentWebsiteInfo') # Field name made lowercase.
    sentattire = models.CharField(max_length=3L, db_column='sentAttire') # Field name made lowercase.
    sentmedicial = models.CharField(max_length=3L, db_column='sentMedicial') # Field name made lowercase.
    sentfinance = models.CharField(max_length=3L, db_column='sentFinance') # Field name made lowercase.
    sentsecurityandsafety = models.CharField(max_length=3L, db_column='sentSecurityAndSafety') # Field name made lowercase.
    sentbiblereading = models.CharField(max_length=3L, db_column='sentBibleReading') # Field name made lowercase.
    senttawelcome = models.CharField(max_length=3L, db_column='sentTAWelcome') # Field name made lowercase.
    sentarrivalinstructions = models.CharField(max_length=3L, db_column='sentArrivalInstructions') # Field name made lowercase.
    sentbrodenniswelcome = models.CharField(max_length=3L, db_column='sentBroDennisWelcome') # Field name made lowercase.
    sentmentor = models.CharField(max_length=3L, db_column='sentMentor') # Field name made lowercase.
    sentbooks = models.CharField(max_length=3L, db_column='sentBooks') # Field name made lowercase.
    class Meta:
        db_table = 'newApplicationsStatus'

class Notesexception(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    description = models.TextField()
    scheduleeventid = models.ForeignKey('Scheduleevent', db_column='scheduleEventID') # Field name made lowercase.
    date = models.DateField()
    class Meta:
        db_table = 'notesException'

class Notesreceived(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    rolleventid = models.ForeignKey('Rollevent', db_column='rollEventID') # Field name made lowercase.
    class Meta:
        db_table = 'notesReceived'

class Page(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=255L, blank=True)
    showinmenu = models.IntegerField(db_column='showInMenu') # Field name made lowercase.
    userid = models.ForeignKey('User', null=True, db_column='userID', blank=True) # Field name made lowercase.
    referrerid = models.IntegerField(null=True, db_column='referrerID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'page'

class Pageaccounttype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    pageid = models.IntegerField(db_column='pageID') # Field name made lowercase.
    accounttypeid = models.IntegerField(db_column='accountTypeID') # Field name made lowercase.
    class Meta:
        db_table = 'pageAccountType'

class Period(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    termid = models.ForeignKey('Term', db_column='termID') # Field name made lowercase.
    periodnumber = models.IntegerField(db_column='periodNumber') # Field name made lowercase.
    startdate = models.DateField(db_column='startDate') # Field name made lowercase.
    enddate = models.DateField(db_column='endDate') # Field name made lowercase.
    class Meta:
        db_table = 'period'

class QuestionEssays(models.Model):
    id = models.IntegerField(primary_key=True)
    promptid = models.IntegerField(null=True, db_column='promptID', blank=True) # Field name made lowercase.
    essay = models.TextField(blank=True)
    termid = models.IntegerField(null=True, db_column='termID', blank=True) # Field name made lowercase.
    traineeid = models.IntegerField(null=True, db_column='traineeID', blank=True) # Field name made lowercase.
    avclassid = models.IntegerField(db_column='avClassID') # Field name made lowercase.
    timestamp = models.DateTimeField()
    class Meta:
        db_table = 'question_essays'

class QuestionPrompts(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=5000L)
    termid = models.IntegerField(null=True, db_column='termID', blank=True) # Field name made lowercase.
    avclassid = models.IntegerField(null=True, db_column='avClassID', blank=True) # Field name made lowercase.
    active = models.IntegerField(null=True, blank=True)
    mid_final = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'question_prompts'

class Recentupdates(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    timestamp = models.CharField(max_length=64L)
    message = models.TextField()
    class Meta:
        db_table = 'recentUpdates'

class Recoveryweekday(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    code = models.CharField(max_length=1L)
    name = models.CharField(max_length=10L)
    class Meta:
        db_table = 'recoveryWeekDay'

class Reportcolumn(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50L)
    code = models.CharField(max_length=50L)
    displayorder = models.IntegerField(null=True, db_column='displayOrder', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'reportColumn'

class Reportcolumnquery(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    reportcolumnid = models.ForeignKey(Reportcolumn, db_column='reportColumnID') # Field name made lowercase.
    reportqueryid = models.ForeignKey('Reportquery', db_column='reportQueryID') # Field name made lowercase.
    class Meta:
        db_table = 'reportColumnQuery'

class Reportquery(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50L)
    query = models.TextField()
    class Meta:
        db_table = 'reportQuery'

class Requestcomment(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    requestid = models.CharField(max_length=50L, db_column='requestID') # Field name made lowercase.
    dateentered = models.DateField(db_column='dateEntered') # Field name made lowercase.
    author = models.CharField(max_length=50L)
    comment = models.TextField()
    class Meta:
        db_table = 'requestComment'

class Requesttracking(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    type = models.CharField(max_length=50L)
    name = models.CharField(max_length=50L)
    description = models.TextField()
    status = models.CharField(max_length=50L)
    priority = models.CharField(max_length=50L)
    startdate = models.DateField(db_column='startDate') # Field name made lowercase.
    actualenddate = models.DateField(db_column='actualEndDate') # Field name made lowercase.
    proposedenddate = models.DateField(db_column='proposedEndDate') # Field name made lowercase.
    assignedto = models.CharField(max_length=50L, db_column='assignedTo') # Field name made lowercase.
    requester = models.CharField(max_length=50L)
    class Meta:
        db_table = 'requestTracking'

class Residence(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100L)
    residencetypeid = models.IntegerField(null=True, db_column='residenceTypeID', blank=True) # Field name made lowercase.
    capacity = models.IntegerField()
    streetaddress = models.CharField(max_length=100L, db_column='streetAddress', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=100L, blank=True)
    state = models.CharField(max_length=2L, blank=True)
    zipcode = models.CharField(max_length=10L, db_column='zipCode', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=24L, blank=True)
    note = models.TextField(blank=True)
    reportseq = models.IntegerField(null=True, db_column='reportSeq', blank=True) # Field name made lowercase.
    fttause = models.IntegerField(db_column='fttaUse') # Field name made lowercase.
    entrycode = models.CharField(max_length=11L, db_column='entryCode', blank=True) # Field name made lowercase.
    availablebeds = models.IntegerField(null=True, db_column='availableBeds', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'residence'

class Residencetype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    residencetype = models.CharField(max_length=5L, db_column='residenceType') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    class Meta:
        db_table = 'residenceType'

class ResidenceRepairs(models.Model):
    id = models.IntegerField(primary_key=True)
    section_id = models.IntegerField()
    room_id = models.IntegerField()
    other_room = models.TextField()
    residence_id = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()
    trainee_id = models.IntegerField()
    active = models.IntegerField()
    completed = models.IntegerField()
    priority = models.IntegerField()
    class Meta:
        db_table = 'residence_repairs'

class ResidenceRoomSections(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'residence_room_sections'

class ResidenceRooms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'residence_rooms'

class Rolldata(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    rolleventid = models.ForeignKey('Rollevent', db_column='rollEventID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    rollstatusid = models.ForeignKey('Rollstatus', db_column='rollStatusID') # Field name made lowercase.
    remarks = models.CharField(max_length=45L, blank=True)
    enteredbyuserid = models.ForeignKey('User', null=True, db_column='enteredByUserID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'rollData'

class Rollevent(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    scheduleeventid = models.IntegerField(db_column='scheduleEventID') # Field name made lowercase.
    date = models.DateField()
    remarks = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'rollEvent'

class Rollstatus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    code = models.CharField(max_length=3L, unique=True)
    name = models.CharField(max_length=15L, unique=True)
    class Meta:
        db_table = 'rollStatus'

class Rollhousefinalization(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    residenceid = models.IntegerField(db_column='residenceID') # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='submitDate') # Field name made lowercase.
    weekstartdate = models.DateTimeField(db_column='weekStartDate') # Field name made lowercase.
    weekenddate = models.DateTimeField(db_column='weekEndDate') # Field name made lowercase.
    class Meta:
        db_table = 'rollhousefinalization'

class Rollsubmissiondata(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='submitDate') # Field name made lowercase.
    startdate = models.DateTimeField(db_column='startDate') # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate') # Field name made lowercase.
    class Meta:
        db_table = 'rollsubmissiondata'

class Rollteamfinalization(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    teamid = models.IntegerField(db_column='teamID') # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='submitDate') # Field name made lowercase.
    weekstartdate = models.DateTimeField(db_column='weekStartDate') # Field name made lowercase.
    weekenddate = models.DateTimeField(db_column='weekEndDate') # Field name made lowercase.
    class Meta:
        db_table = 'rollteamfinalization'

class Rollypcfinalization(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='submitDate') # Field name made lowercase.
    weekstartdate = models.DateTimeField(db_column='weekStartDate') # Field name made lowercase.
    weekenddate = models.DateTimeField(db_column='weekEndDate') # Field name made lowercase.
    class Meta:
        db_table = 'rollypcfinalization'

class Room(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    residenceid = models.IntegerField(db_column='residenceID') # Field name made lowercase.
    capacity = models.IntegerField()
    class Meta:
        db_table = 'room'

class Roomlist(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=100L)
    location = models.CharField(max_length=255L)
    status = models.CharField(max_length=1L)
    class Meta:
        db_table = 'roomlist'

class Roomreservationrequests(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    content = models.TextField(blank=True)
    room = models.CharField(max_length=11L)
    groupsize = models.IntegerField(db_column='groupSize') # Field name made lowercase.
    frequency = models.TextField()
    date = models.DateField()
    starttime = models.TextField(db_column='startTime') # Field name made lowercase. This field type is a guess.
    endtime = models.TextField(db_column='endTime') # Field name made lowercase. This field type is a guess.
    duration = models.FloatField()
    reason = models.TextField()
    status = models.CharField(max_length=20L)
    reminderflag = models.IntegerField(db_column='reminderFlag') # Field name made lowercase.
    timestamp = models.DateTimeField()
    fellowshipwith = models.IntegerField(null=True, db_column='fellowshipWith', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'roomreservationrequests'

class Roomschedule(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    timestamp = models.DateTimeField()
    date = models.DateField()
    time = models.CharField(max_length=10L)
    roomid = models.IntegerField(db_column='roomID') # Field name made lowercase.
    content = models.CharField(max_length=255L)
    class Meta:
        db_table = 'roomschedule'

class RsMinistrybooks(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField()
    code = models.TextField()
    cartnumber = models.CharField(max_length=10L, db_column='cartNumber', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'rs_ministryBooks'

class RsSyllabus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    trainingclassesid = models.IntegerField(db_column='trainingClassesID') # Field name made lowercase.
    date = models.DateField()
    topic = models.TextField(blank=True)
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    classtype = models.CharField(max_length=8L, db_column='classType') # Field name made lowercase.
    class Meta:
        db_table = 'rs_syllabus'

class RsSyllabusreadings(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    rs_syllabusid = models.IntegerField(db_column='rs_syllabusID') # Field name made lowercase.
    rs_ministrybooksid = models.IntegerField(null=True, db_column='rs_ministrybooksID', blank=True) # Field name made lowercase.
    readings = models.CharField(max_length=255L)
    class Meta:
        db_table = 'rs_syllabusReadings'

class Savedreport(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'savedReport'

class Savedreportcolumn(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    savedreportid = models.ForeignKey(Savedreport, db_column='savedReportID') # Field name made lowercase.
    reportcolumnid = models.ForeignKey(Reportcolumn, db_column='reportColumnID') # Field name made lowercase.
    class Meta:
        db_table = 'savedReportColumn'

class Schedule(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100L)
    comments = models.CharField(max_length=100L, blank=True)
    startdate = models.DateField(null=True, db_column='startDate', blank=True) # Field name made lowercase.
    enddate = models.DateField(null=True, db_column='endDate', blank=True) # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    schedulecategoryid = models.IntegerField(db_column='scheduleCategoryID') # Field name made lowercase.
    priority = models.BigIntegerField()
    accounttypeid = models.ForeignKey(Accounttype, null=True, db_column='accountTypeID', blank=True) # Field name made lowercase.
    display = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'schedule'

class Schedulecategory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'scheduleCategory'

class Scheduleevent(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    scheduleid = models.ForeignKey(Schedule, db_column='scheduleID') # Field name made lowercase.
    weekdayid = models.ForeignKey('Weekday', db_column='weekDayID') # Field name made lowercase.
    starttime = models.TextField(db_column='startTime') # Field name made lowercase. This field type is a guess.
    endtime = models.TextField(db_column='endTime') # Field name made lowercase. This field type is a guess.
    name = models.CharField(max_length=45L, blank=True)
    code = models.CharField(max_length=15L)
    isclass = models.IntegerField(db_column='isClass') # Field name made lowercase.
    isroll = models.IntegerField(db_column='isRoll') # Field name made lowercase.
    class Meta:
        db_table = 'scheduleEvent'

class Scheduletraineefilter(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    scheduleid = models.ForeignKey(Schedule, db_column='scheduleID') # Field name made lowercase.
    traineefilterid = models.ForeignKey('Traineefilter', db_column='traineeFilterID') # Field name made lowercase.
    class Meta:
        db_table = 'scheduleTraineeFilter'

class Seat(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    seatx = models.IntegerField(db_column='seatX') # Field name made lowercase.
    seaty = models.IntegerField(db_column='seatY') # Field name made lowercase.
    seatingchartid = models.ForeignKey('Seatingchart', db_column='seatingChartID') # Field name made lowercase.
    class Meta:
        db_table = 'seat'

class Seating(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    seatid = models.ForeignKey(Seat, db_column='seatID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', null=True, db_column='traineeID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'seating'

class Seatingchart(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    seatingchartname = models.CharField(max_length=50L, unique=True, db_column='seatingChartName') # Field name made lowercase.
    class Meta:
        db_table = 'seatingChart'

class Seatingevent(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    seatingchartid = models.ForeignKey(Seatingchart, db_column='seatingChartID') # Field name made lowercase.
    scheduleeventid = models.ForeignKey(Scheduleevent, db_column='scheduleEventID') # Field name made lowercase.
    class Meta:
        db_table = 'seatingEvent'

class Semiannualstudyattendance(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    location = models.TextField()
    d1 = models.CharField(max_length=1L)
    d2 = models.CharField(max_length=1L)
    d3 = models.CharField(max_length=1L)
    d4 = models.CharField(max_length=1L)
    d5 = models.CharField(max_length=1L)
    class Meta:
        db_table = 'semiAnnualStudyAttendance'

class Semiannualstudylocation(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    location = models.CharField(max_length=5L)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = 'semiAnnualStudyLocation'

class Semiannualtesting(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    groupnumber = models.IntegerField(null=True, db_column='groupNumber', blank=True) # Field name made lowercase.
    servicecode = models.CharField(max_length=1L, db_column='serviceCode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'semiAnnualTesting'

class Semiannualtestingrooms(models.Model):
    groupnumber = models.IntegerField(db_column='groupNumber') # Field name made lowercase.
    gender = models.CharField(max_length=1L)
    year = models.CharField(max_length=1L)
    room = models.TextField()
    class Meta:
        db_table = 'semiAnnualTestingRooms'

class Sendinglocality(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    localityid = models.IntegerField(db_column='localityID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    class Meta:
        db_table = 'sendingLocality'

class Svassignment(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    svserviceworkergroupid = models.ForeignKey('Svserviceworkergroup', db_column='svServiceWorkerGroupID') # Field name made lowercase.
    svscheduleinstanceid = models.ForeignKey('Svscheduleinstance', db_column='svScheduleInstanceID') # Field name made lowercase.
    class Meta:
        db_table = 'svAssignment'

class Svassignmentsave(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    svserviceworkergroupid = models.IntegerField(db_column='svServiceWorkerGroupID') # Field name made lowercase.
    svscheduleinstanceid = models.IntegerField(db_column='svScheduleInstanceID') # Field name made lowercase.
    class Meta:
        db_table = 'svAssignmentSave'

class Svexception(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    startdate = models.DateField(null=True, db_column='startDate', blank=True) # Field name made lowercase.
    enddate = models.DateField(null=True, db_column='endDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svException'

class Svexceptionservice(models.Model):
    id = models.IntegerField(primary_key=True)
    svexceptionid = models.IntegerField(null=True, db_column='svExceptionID', blank=True) # Field name made lowercase.
    svserviceid = models.IntegerField(null=True, db_column='svServiceID', blank=True) # Field name made lowercase.
    svservicescheduleid = models.IntegerField(null=True, db_column='svServiceScheduleID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svExceptionService'

class Svexceptiontrainee(models.Model):
    id = models.IntegerField(primary_key=True)
    svexceptionid = models.IntegerField(null=True, db_column='svExceptionID', blank=True) # Field name made lowercase.
    traineeid = models.IntegerField(null=True, db_column='traineeID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svExceptionTrainee'

class Svmissedservice(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    svscheduleinstanceid = models.IntegerField(db_column='svScheduleInstanceID') # Field name made lowercase.
    svserviceworkergroupid = models.IntegerField(db_column='svServiceWorkerGroupID') # Field name made lowercase.
    class Meta:
        db_table = 'svMissedService'

class Svnote(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField(blank=True)
    data = models.TextField(blank=True)
    norder = models.FloatField(null=True, blank=True)
    userid = models.ForeignKey('User', null=True, db_column='userID', blank=True) # Field name made lowercase.
    moddate = models.DateTimeField(db_column='modDate') # Field name made lowercase.
    class Meta:
        db_table = 'svNote'

class Svpermanentassignment(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    svserviceworkergroupid = models.ForeignKey('Svserviceworkergroup', db_column='svServiceWorkerGroupID') # Field name made lowercase.
    active = models.IntegerField()
    class Meta:
        db_table = 'svPermanentAssignment'

class Svqualificationgroup(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    traineefilterid = models.ForeignKey('Traineefilter', db_column='traineeFilterID') # Field name made lowercase.
    class Meta:
        db_table = 'svQualificationGroup'

class Svreport(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50L)
    description = models.CharField(max_length=255L, blank=True)
    headermessage = models.TextField(db_column='headerMessage', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svReport'

class Svreportnote(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    note = models.TextField()
    reporttype = models.CharField(max_length=511L, db_column='reportType', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svReportNote'

class Svreportservice(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svreportid = models.IntegerField(db_column='svReportID') # Field name made lowercase.
    svserviceid = models.IntegerField(db_column='svServiceID') # Field name made lowercase.
    sortorder = models.IntegerField(db_column='sortOrder') # Field name made lowercase.
    class Meta:
        db_table = 'svReportService'

class Svreporttraineecomment(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svscheduleinstanceid = models.ForeignKey('Svscheduleinstance', db_column='svScheduleInstanceID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    comment = models.TextField(blank=True)
    class Meta:
        db_table = 'svReportTraineeComment'

class Svrolldata(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svrolleventid = models.ForeignKey('Svrollevent', db_column='svRollEventID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    substitutetraineeid = models.ForeignKey('Trainee', db_column='substituteTraineeID', related_name='svrolldata+') # Field name made lowercase.
    isvolunteer = models.IntegerField(db_column='isVolunteer') # Field name made lowercase.
    rollstatusid = models.ForeignKey(Rollstatus, db_column='rollStatusID') # Field name made lowercase.
    remarks = models.CharField(max_length=45L)
    class Meta:
        db_table = 'svRollData'

class Svrollevent(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userID') # Field name made lowercase.
    svservicetimeid = models.ForeignKey('Svservicetime', db_column='svServiceTimeID') # Field name made lowercase.
    date = models.DateTimeField()
    remarks = models.CharField(max_length=45L)
    class Meta:
        db_table = 'svRollEvent'

class Svscheduleinstance(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.ForeignKey('User', null=True, db_column='userID', blank=True) # Field name made lowercase.
    svservicescheduleid = models.IntegerField(db_column='svServiceScheduleID') # Field name made lowercase.
    startdate = models.DateField(null=True, db_column='startDate', blank=True) # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='modifiedTime') # Field name made lowercase.
    class Meta:
        db_table = 'svScheduleInstance'

class Svservice(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive') # Field name made lowercase.
    svservicecategoryid = models.ForeignKey('Svservicecategory', db_column='svServiceCategoryID') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    suffix = models.CharField(max_length=10L)
    svservicesorttypeid = models.ForeignKey('Svservicesorttype', db_column='svServiceSortTypeID') # Field name made lowercase.
    weight = models.IntegerField()
    class Meta:
        db_table = 'svService'

class Svservicealgorithm(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svservicesorttypeid = models.IntegerField(db_column='svServiceSortTypeID') # Field name made lowercase.
    emphasis = models.IntegerField(null=True, blank=True)
    value = models.FloatField()
    class Meta:
        db_table = 'svServiceAlgorithm'

class Svservicecategory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    description = models.TextField()
    class Meta:
        db_table = 'svServiceCategory'

class Svserviceschedule(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'svServiceSchedule'

class Svservicesorttype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.TextField()
    description = models.TextField()
    code = models.CharField(max_length=3L, unique=True)
    class Meta:
        db_table = 'svServiceSortType'

class Svservicetime(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svserviceid = models.ForeignKey(Svservice, db_column='svServiceID') # Field name made lowercase.
    svservicescheduleid = models.IntegerField(db_column='svServiceScheduleID') # Field name made lowercase.
    week = models.IntegerField(null=True, blank=True)
    weekdayid = models.ForeignKey('Weekday', db_column='weekDayID', related_name='svservicetime+') # Field name made lowercase.
    starttime = models.TextField(db_column='startTime') # Field name made lowercase. This field type is a guess.
    endtime = models.TextField(db_column='endTime', blank=True) # Field name made lowercase. This field type is a guess.
    weekdayid2 = models.IntegerField(db_column='weekDayID2') # Field name made lowercase.
    starttime2 = models.TextField(db_column='startTime2') # Field name made lowercase. This field type is a guess.
    endtime2 = models.TextField(db_column='endTime2', blank=True) # Field name made lowercase. This field type is a guess.
    hidden_value2 = models.IntegerField()
    weekdayid3 = models.IntegerField(db_column='weekDayID3') # Field name made lowercase.
    starttime3 = models.TextField(db_column='startTime3') # Field name made lowercase. This field type is a guess.
    endtime3 = models.TextField(db_column='endTime3', blank=True) # Field name made lowercase. This field type is a guess.
    hidden_value3 = models.IntegerField()
    recoveryweekdayid = models.ForeignKey('Weekday', db_column='recoveryWeekDayID', related_name='svservicetime') # Field name made lowercase.
    recoverytime = models.TextField(db_column='recoveryTime', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'svServiceTime'

class Svservicetimescheduleevent(models.Model):
    svservicetimeid = models.IntegerField(db_column='svServiceTimeID') # Field name made lowercase.
    scheduleeventid = models.IntegerField(db_column='scheduleEventID') # Field name made lowercase.
    class Meta:
        db_table = 'svServiceTimeScheduleEvent'

class Svservicetoschedulemap(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svservicescheduleid = models.IntegerField(db_column='svServiceScheduleID') # Field name made lowercase.
    svserviceid = models.IntegerField(db_column='svServiceID') # Field name made lowercase.
    class Meta:
        db_table = 'svServiceToScheduleMap'

class Svservicetraineefilter(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svserviceid = models.ForeignKey(Svservice, db_column='svServiceID') # Field name made lowercase.
    traineefilterid = models.ForeignKey('Traineefilter', db_column='traineeFilterID') # Field name made lowercase.
    class Meta:
        db_table = 'svServiceTraineeFilter'

class Svserviceweeklyreport(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    svserviceid = models.IntegerField(db_column='svServiceID') # Field name made lowercase.
    weekid = models.IntegerField(db_column='weekID') # Field name made lowercase.
    termid = models.IntegerField(db_column='termID') # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate') # Field name made lowercase.
    class Meta:
        db_table = 'svServiceWeeklyReport'

class Svserviceweeklyreportentry(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svserviceweeklyreportid = models.IntegerField(db_column='svServiceWeeklyReportID') # Field name made lowercase.
    dayid = models.IntegerField(db_column='dayID') # Field name made lowercase.
    starttime = models.TextField(db_column='startTime', blank=True) # Field name made lowercase. This field type is a guess.
    endtime = models.TextField(db_column='endTime', blank=True) # Field name made lowercase. This field type is a guess.
    taskperformed = models.TextField(db_column='taskPerformed', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svServiceWeeklyReportEntry'

class Svserviceworkergroup(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    suffix = models.CharField(max_length=10L)
    svserviceid = models.ForeignKey(Svservice, db_column='svServiceID') # Field name made lowercase.
    numberofworkers = models.IntegerField(db_column='numberOfWorkers') # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive') # Field name made lowercase.
    svservicescheduleid = models.IntegerField(null=True, db_column='svServiceScheduleID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svServiceWorkerGroup'

class Svserviceworkergroupsnapshot(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svscheduleinstanceid = models.ForeignKey(Svscheduleinstance, db_column='svScheduleInstanceID') # Field name made lowercase.
    svserviceworkergroupid = models.ForeignKey(Svserviceworkergroup, db_column='svServiceWorkerGroupID') # Field name made lowercase.
    numberofworkers = models.IntegerField(db_column='numberOfWorkers') # Field name made lowercase.
    class Meta:
        db_table = 'svServiceWorkerGroupSnapshot'

class Svserviceworkergrouptraineefilter(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svserviceworkergroupid = models.ForeignKey(Svserviceworkergroup, db_column='svServiceWorkerGroupID') # Field name made lowercase.
    traineefilterid = models.ForeignKey('Traineefilter', db_column='traineeFilterID') # Field name made lowercase.
    class Meta:
        db_table = 'svServiceWorkerGroupTraineeFilter'

class Svworkerexception(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    svserviceid = models.ForeignKey(Svservice, null=True, db_column='svServiceID', blank=True) # Field name made lowercase.
    startdate = models.DateField(db_column='startDate') # Field name made lowercase.
    enddate = models.DateField(null=True, db_column='endDate', blank=True) # Field name made lowercase.
    reason = models.TextField(blank=True)
    class Meta:
        db_table = 'svWorkerException'

class Svworkerqualification(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.ForeignKey('Trainee', db_column='traineeID') # Field name made lowercase.
    svqualificationgroupid = models.ForeignKey(Svqualificationgroup, db_column='svQualificationGroupID') # Field name made lowercase.
    class Meta:
        db_table = 'svWorkerQualification'

class Svworkloadhistory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    oldworkload = models.IntegerField(db_column='oldWorkload') # Field name made lowercase.
    date = models.DateField()
    class Meta:
        db_table = 'svWorkloadHistory'

class Svserviceview(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    suffix = models.CharField(max_length=10L)
    isactive = models.IntegerField(db_column='isActive') # Field name made lowercase.
    categoryid = models.IntegerField(null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    categoryname = models.CharField(max_length=45L, db_column='categoryName', blank=True) # Field name made lowercase.
    servicefilterlookupid = models.IntegerField(null=True, db_column='serviceFilterLookupID', blank=True) # Field name made lowercase.
    servicefilterid = models.IntegerField(null=True, db_column='serviceFilterID', blank=True) # Field name made lowercase.
    servicefiltername = models.CharField(max_length=255L, db_column='serviceFilterName', blank=True) # Field name made lowercase.
    workergrpid = models.IntegerField(null=True, db_column='workerGrpID', blank=True) # Field name made lowercase.
    workergrpname = models.CharField(max_length=45L, db_column='workerGrpName', blank=True) # Field name made lowercase.
    workergrpsuffix = models.CharField(max_length=10L, db_column='workerGrpSuffix', blank=True) # Field name made lowercase.
    workergrpisactive = models.IntegerField(null=True, db_column='workerGrpIsActive', blank=True) # Field name made lowercase.
    workergrpfilterlookupid = models.IntegerField(null=True, db_column='workerGrpFilterLookupID', blank=True) # Field name made lowercase.
    workergrpfilterid = models.IntegerField(null=True, db_column='workerGrpFilterID', blank=True) # Field name made lowercase.
    workergrpfiltername = models.CharField(max_length=255L, db_column='workerGrpFilterName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'svserviceview'

class Team(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100L)
    code = models.CharField(max_length=15L)
    teamtypeid = models.IntegerField(db_column='teamTypeID') # Field name made lowercase.
    trainerusername = models.CharField(max_length=45L, db_column='trainerUserName') # Field name made lowercase.
    bromonitortraineeid = models.IntegerField(db_column='broMonitorTraineeID') # Field name made lowercase.
    sismonitortraineeid = models.IntegerField(db_column='sisMonitorTraineeID') # Field name made lowercase.
    class Meta:
        db_table = 'team'

class Teamschedule(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    teamid = models.IntegerField(db_column='teamID') # Field name made lowercase.
    scheduleid = models.IntegerField(db_column='scheduleID') # Field name made lowercase.
    class Meta:
        db_table = 'teamSchedule'

class Teamtype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    description = models.CharField(max_length=100L)
    class Meta:
        db_table = 'teamType'

class Term(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=45L)
    startdate = models.CharField(max_length=10L, db_column='startDate') # Field name made lowercase.
    enddate = models.CharField(max_length=10L, db_column='endDate') # Field name made lowercase.
    taskstage = models.IntegerField(null=True, db_column='taskStage', blank=True) # Field name made lowercase.
    taskscompleted = models.IntegerField(null=True, db_column='tasksCompleted', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'term'

class Tmplsimportoffense(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    lastfirst = models.CharField(max_length=50L, db_column='lastFirst') # Field name made lowercase.
    level = models.CharField(max_length=7L)
    offensereason = models.CharField(max_length=30L, db_column='offenseReason') # Field name made lowercase.
    numlsowed = models.IntegerField(db_column='numLSOwed') # Field name made lowercase.
    manualhandling = models.IntegerField(db_column='manualHandling') # Field name made lowercase.
    importsignedin = models.IntegerField(db_column='importSignedIn') # Field name made lowercase.
    fullyturnedin = models.IntegerField(db_column='FullyTurnedIn') # Field name made lowercase.
    dns = models.IntegerField(db_column='DNS') # Field name made lowercase.
    wnr = models.IntegerField(db_column='WNR') # Field name made lowercase.
    snc = models.IntegerField(db_column='SNC') # Field name made lowercase.
    numlsreceived = models.IntegerField(db_column='numLSReceived') # Field name made lowercase.
    lastupdatedate = models.DateField(db_column='lastUpdateDate') # Field name made lowercase.
    datedue = models.DateField(null=True, db_column='DateDue', blank=True) # Field name made lowercase.
    comments = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'tmpLsImportOffense'

class Trainee(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.ForeignKey('User', unique=True, null=True, db_column='userID', blank=True, related_name='trainee+') # Field name made lowercase.
    datebegin = models.DateField(null=True, db_column='dateBegin', blank=True) # Field name made lowercase.
    dateend = models.DateField(null=True, db_column='dateEnd', blank=True) # Field name made lowercase.
    firstterm_termid = models.ForeignKey(Term, null=True, db_column='firstTerm_termID', blank=True) # Field name made lowercase.
    secondterm_termid = models.ForeignKey(Term, null=True, db_column='secondTerm_termID', blank=True, related_name='trainee+') # Field name made lowercase.
    thirdterm_termid = models.ForeignKey(Term, null=True, db_column='thirdTerm_termID', blank=True, related_name='trainee+') # Field name made lowercase.
    fourthterm_termid = models.ForeignKey(Term, null=True, db_column='fourthTerm_termID', blank=True, related_name='trainee+') # Field name made lowercase.
    termscompleted = models.IntegerField(null=True, db_column='termsCompleted', blank=True) # Field name made lowercase.
    active = models.IntegerField()
    couple = models.IntegerField()
    emergencycontact = models.CharField(max_length=32L, db_column='emergencyContact', blank=True) # Field name made lowercase.
    emergencyaddress = models.TextField(db_column='emergencyAddress', blank=True) # Field name made lowercase.
    emergencyphonenumber = models.CharField(max_length=32L, db_column='emergencyPhoneNumber', blank=True) # Field name made lowercase.
    emergencyphonenumber2 = models.CharField(max_length=14L, db_column='emergencyPhoneNumber2', blank=True) # Field name made lowercase.
    readoldtestament = models.IntegerField(db_column='readOldTestament') # Field name made lowercase.
    readnewtestament = models.IntegerField(db_column='readNewTestament') # Field name made lowercase.
    trainingassistantid = models.ForeignKey('Trainingassistant', null=True, db_column='trainingAssistantID', blank=True) # Field name made lowercase.
    mentor_userid = models.ForeignKey('User', null=True, db_column='mentor_userID', blank=True, related_name='trainee') # Field name made lowercase.
    mentor = models.CharField(max_length=50L, blank=True)
    college = models.CharField(max_length=255L, blank=True)
    major = models.CharField(max_length=255L, blank=True)
    degree = models.TextField(blank=True)
    gospelpreference1 = models.CharField(max_length=255L, db_column='gospelPreference1', blank=True) # Field name made lowercase.
    gospelpreference2 = models.CharField(max_length=255L, db_column='gospelPreference2', blank=True) # Field name made lowercase.
    vehicleinfoold = models.CharField(max_length=50L, db_column='vehicleInfoOld', blank=True) # Field name made lowercase.
    vehiclemakeold = models.CharField(max_length=255L, db_column='vehicleMakeOld', blank=True) # Field name made lowercase.
    vehiclemodelold = models.CharField(max_length=255L, db_column='vehicleModelOld', blank=True) # Field name made lowercase.
    vehicleyearold = models.IntegerField(null=True, db_column='vehicleYearOld', blank=True) # Field name made lowercase.
    vehicleyesno = models.IntegerField(db_column='vehicleYesNo') # Field name made lowercase.
    vehiclemodel = models.CharField(max_length=50L, db_column='vehicleModel', blank=True) # Field name made lowercase.
    vehiclelicense = models.CharField(max_length=50L, db_column='vehicleLicense', blank=True) # Field name made lowercase.
    vehiclecolor = models.CharField(max_length=50L, db_column='vehicleColor', blank=True) # Field name made lowercase.
    vehiclecapacity = models.FloatField(null=True, db_column='vehicleCapacity', blank=True) # Field name made lowercase.
    teamid = models.IntegerField(null=True, db_column='teamID', blank=True) # Field name made lowercase.
    residenceid = models.ForeignKey(Residence, null=True, db_column='residenceID', blank=True) # Field name made lowercase.
    greekcharacter = models.CharField(max_length=1L)
    svservicesleft = models.IntegerField(null=True, db_column='svServicesLeft', blank=True) # Field name made lowercase.
    officeid = models.IntegerField(null=True, db_column='officeID', blank=True) # Field name made lowercase.
    traineestatusid = models.ForeignKey('Traineestatus', db_column='traineeStatusID') # Field name made lowercase.
    bunkid = models.IntegerField(null=True, db_column='bunkID', blank=True) # Field name made lowercase.
    mrtype = models.IntegerField(null=True, db_column='MRType', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'trainee'

class Traineefilter(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=255L)
    filter = models.TextField(blank=True)
    class Meta:
        db_table = 'traineeFilter'

class Traineeschedule(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(db_column='traineeID') # Field name made lowercase.
    scheduleid = models.ForeignKey(Schedule, db_column='scheduleID') # Field name made lowercase.
    startdate = models.DateField(null=True, db_column='startDate', blank=True) # Field name made lowercase.
    enddate = models.DateField(null=True, db_column='endDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'traineeSchedule'

class Traineestatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    class Meta:
        db_table = 'traineeStatus'

class TraineeOld(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(unique=True, null=True, db_column='userID', blank=True) # Field name made lowercase.
    lastname = models.TextField(db_column='lastName') # Field name made lowercase.
    firstname = models.TextField(db_column='firstName') # Field name made lowercase.
    middlename = models.TextField(db_column='middleName', blank=True) # Field name made lowercase.
    birthdate = models.DateField(null=True, db_column='birthDate', blank=True) # Field name made lowercase.
    sendinglocality = models.TextField(db_column='sendingLocality', blank=True) # Field name made lowercase.
    gender = models.CharField(max_length=1L)
    termscompleted = models.IntegerField(null=True, db_column='termsCompleted', blank=True) # Field name made lowercase.
    active = models.IntegerField(null=True, blank=True)
    datebegin = models.DateField(null=True, db_column='dateBegin', blank=True) # Field name made lowercase.
    dateend = models.DateField(null=True, db_column='dateEnd', blank=True) # Field name made lowercase.
    maritalstatus = models.CharField(max_length=1L, db_column='maritalStatus', blank=True) # Field name made lowercase.
    residenceid = models.IntegerField(null=True, db_column='residenceID', blank=True) # Field name made lowercase.
    cellphone = models.CharField(max_length=30L, db_column='cellPhone', blank=True) # Field name made lowercase.
    teamid = models.IntegerField(null=True, db_column='teamID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'trainee_old'

class Traineeview(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    name = models.CharField(max_length=65L)
    lastfirst = models.CharField(max_length=66L, db_column='lastFirst') # Field name made lowercase.
    firstname = models.CharField(max_length=32L, db_column='firstName') # Field name made lowercase.
    lastname = models.CharField(max_length=32L, db_column='lastName') # Field name made lowercase.
    middlename = models.CharField(max_length=32L, db_column='middleName', blank=True) # Field name made lowercase.
    birthdate = models.DateField(null=True, db_column='birthDate', blank=True) # Field name made lowercase.
    gender = models.CharField(max_length=1L, blank=True)
    active = models.IntegerField(null=True, blank=True)
    traineestatusid = models.IntegerField(db_column='traineeStatusID') # Field name made lowercase.
    traineestatus = models.TextField(db_column='traineeStatus', blank=True) # Field name made lowercase.
    maritalstatus = models.CharField(max_length=1L, db_column='maritalStatus', blank=True) # Field name made lowercase.
    couple = models.IntegerField()
    greekcharacter = models.CharField(max_length=1L)
    cellphone = models.CharField(max_length=14L, db_column='cellPhone', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=32L)
    sendinglocality = models.TextField(db_column='sendingLocality', blank=True) # Field name made lowercase.
    termscompleted = models.IntegerField(null=True, db_column='termsCompleted', blank=True) # Field name made lowercase.
    datebegin = models.DateField(null=True, db_column='dateBegin', blank=True) # Field name made lowercase.
    dateend = models.DateField(null=True, db_column='dateEnd', blank=True) # Field name made lowercase.
    residenceid = models.IntegerField(null=True, db_column='residenceID', blank=True) # Field name made lowercase.
    residencename = models.CharField(max_length=100L, db_column='residenceName', blank=True) # Field name made lowercase.
    teamid = models.IntegerField(null=True, db_column='teamID', blank=True) # Field name made lowercase.
    teamname = models.CharField(max_length=100L, db_column='teamName', blank=True) # Field name made lowercase.
    teamcode = models.CharField(max_length=15L, db_column='teamCode', blank=True) # Field name made lowercase.
    teamtrainer = models.CharField(max_length=45L, db_column='teamTrainer', blank=True) # Field name made lowercase.
    svservicesleft = models.IntegerField(null=True, db_column='svServicesLeft', blank=True) # Field name made lowercase.
    trainingassistantid = models.IntegerField(null=True, db_column='trainingAssistantID', blank=True) # Field name made lowercase.
    trainingassistantname = models.CharField(max_length=65L, db_column='trainingAssistantName', blank=True) # Field name made lowercase.
    vehicleinfo = models.FloatField(null=True, db_column='vehicleInfo', blank=True) # Field name made lowercase.
    vehiclemake = models.CharField(max_length=50L, db_column='vehicleMake', blank=True) # Field name made lowercase.
    vehiclemodel = models.CharField(max_length=50L, db_column='vehicleModel', blank=True) # Field name made lowercase.
    vehicleyear = models.CharField(max_length=50L, db_column='vehicleYear', blank=True) # Field name made lowercase.
    vehiclelicense = models.CharField(max_length=50L, db_column='vehicleLicense', blank=True) # Field name made lowercase.
    vehiclecolor = models.CharField(max_length=50L, db_column='vehicleColor', blank=True) # Field name made lowercase.
    vehiclecapacity = models.FloatField(null=True, db_column='vehicleCapacity', blank=True) # Field name made lowercase.
    teamtypeid = models.IntegerField(null=True, db_column='teamTypeID', blank=True) # Field name made lowercase.
    teamtype = models.CharField(max_length=100L, db_column='teamType', blank=True) # Field name made lowercase.
    officeid = models.IntegerField(null=True, db_column='officeID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'traineeview'

class Trainingassistant(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userID') # Field name made lowercase.
    lastname = models.CharField(max_length=32L, db_column='lastName') # Field name made lowercase.
    firstname = models.CharField(max_length=32L, db_column='firstName') # Field name made lowercase.
    middlename = models.CharField(max_length=32L, db_column='middleName', blank=True) # Field name made lowercase.
    birthdate = models.DateTimeField(null=True, db_column='birthDate', blank=True) # Field name made lowercase.
    active = models.IntegerField()
    maritalstatus = models.CharField(max_length=1L, db_column='maritalStatus', blank=True) # Field name made lowercase.
    residence = models.IntegerField(null=True, blank=True)
    outoftown = models.IntegerField(null=True, db_column='outOfTown', blank=True) # Field name made lowercase.
    approvingtaid = models.IntegerField(null=True, db_column='approvingTAID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'trainingAssistant'

class Trainingclasses(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50L)
    code = models.TextField()
    weekdayid = models.IntegerField(db_column='weekdayID') # Field name made lowercase.
    readwhen = models.IntegerField(db_column='readWhen') # Field name made lowercase.
    year = models.CharField(max_length=6L)
    hassyllabus = models.IntegerField(db_column='hasSyllabus') # Field name made lowercase.
    secode = models.TextField(db_column='seCode') # Field name made lowercase.
    class Meta:
        db_table = 'trainingClasses'

class Trainingassistantview(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    name = models.CharField(max_length=65L)
    lastfirst = models.CharField(max_length=66L, db_column='lastFirst') # Field name made lowercase.
    firstname = models.CharField(max_length=32L, db_column='firstName') # Field name made lowercase.
    lastname = models.CharField(max_length=32L, db_column='lastName') # Field name made lowercase.
    outoftown = models.IntegerField(null=True, db_column='outOfTown', blank=True) # Field name made lowercase.
    approvingtaid = models.IntegerField(null=True, db_column='approvingTAID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'trainingassistantview'

class User(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    username = models.CharField(max_length=32L, unique=True)
    encryptedpassword = models.CharField(max_length=32L, db_column='encryptedPassword', blank=True) # Field name made lowercase.
    firstname = models.CharField(max_length=32L, db_column='firstName') # Field name made lowercase.
    nickname = models.CharField(max_length=32L, db_column='nickName', blank=True) # Field name made lowercase.
    lastname = models.CharField(max_length=32L, db_column='lastName') # Field name made lowercase.
    middlename = models.CharField(max_length=32L, db_column='middleName', blank=True) # Field name made lowercase.
    maidenname = models.CharField(max_length=32L, db_column='maidenName', blank=True) # Field name made lowercase.
    birthdate = models.DateField(null=True, db_column='birthDate', blank=True) # Field name made lowercase.
    gender = models.CharField(max_length=1L, blank=True)
    home_localityid = models.IntegerField(null=True, db_column='home_localityID', blank=True) # Field name made lowercase.
    address = models.CharField(max_length=255L, blank=True)
    city = models.CharField(max_length=255L, blank=True)
    state = models.CharField(max_length=255L, blank=True)
    zip = models.CharField(max_length=10L, blank=True)
    country = models.CharField(max_length=255L, blank=True)
    active = models.IntegerField(null=True, blank=True)
    maritalstatus = models.CharField(max_length=1L, db_column='maritalStatus', blank=True) # Field name made lowercase.
    homephone = models.CharField(max_length=14L, db_column='homePhone', blank=True) # Field name made lowercase.
    cellphone = models.CharField(max_length=14L, db_column='cellPhone', blank=True) # Field name made lowercase.
    workphone = models.TextField(db_column='workPhone', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=255L, blank=True)
    lastlogin = models.DateTimeField(null=True, db_column='lastLogin', blank=True) # Field name made lowercase.
    lastip = models.CharField(max_length=15L, db_column='lastIP', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'user'

class Useraccounttype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.ForeignKey(User, db_column='userID') # Field name made lowercase.
    accounttypeid = models.ForeignKey(Accounttype, db_column='accountTypeID') # Field name made lowercase.
    class Meta:
        db_table = 'userAccountType'

class Waapprovalstatus(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    approvalstatus = models.CharField(max_length=12L, db_column='approvalStatus') # Field name made lowercase.
    class Meta:
        db_table = 'waApprovalStatus'

class Wamaclist(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    mac = models.CharField(max_length=17L)
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    comments = models.TextField()
    class Meta:
        db_table = 'waMACList'

class Wareason(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    reason = models.CharField(max_length=32L)
    class Meta:
        db_table = 'waReason'

class Warequest(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    traineeid = models.IntegerField(null=True, db_column='traineeID', blank=True) # Field name made lowercase.
    wareasonid = models.IntegerField(db_column='waReasonID') # Field name made lowercase.
    minutes = models.IntegerField(null=True, blank=True)
    submissiondate = models.DateTimeField(db_column='submissionDate') # Field name made lowercase.
    timestart = models.DateTimeField(null=True, blank=True)
    mac = models.CharField(max_length=17L, db_column='MAC') # Field name made lowercase.
    waapprovalstatusid = models.IntegerField(db_column='waApprovalStatusID') # Field name made lowercase.
    comments = models.TextField()
    usagetime = models.TextField(db_column='usageTime', blank=True) # Field name made lowercase.
    usagedate = models.DateField(db_column='usageDate') # Field name made lowercase.
    tacomments = models.TextField(db_column='TAComments', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'waRequest'

class Weatherlocation(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=32L)
    zip = models.CharField(max_length=5L)
    lat = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=4, blank=True)
    active = models.IntegerField()
    updated = models.DateTimeField(null=True, blank=True)
    cache = models.TextField(blank=True)
    class Meta:
        db_table = 'weatherLocation'

class Weekday(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    code = models.CharField(max_length=1L)
    name = models.CharField(max_length=10L)
    dayorder = models.FloatField(null=True, db_column='dayOrder', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'weekDay'

