# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AId(models.Model):
    userid = models.BigIntegerField(db_column='userId', unique=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a_id'


class AnalysisSOrder(models.Model):
    dt = models.DateField()
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    pro_big_type = models.CharField(max_length=255, blank=True, null=True)
    pro_type = models.CharField(max_length=255, blank=True, null=True)
    date_type = models.IntegerField()
    v_type = models.CharField(max_length=255)
    person_num = models.IntegerField()
    order_num = models.IntegerField()
    order_totalfee = models.FloatField()
    reference_price_paid = models.FloatField()
    updatetime = models.DateTimeField()
    createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'analysis_s_order'


class AnalysisWxChatWord(models.Model):
    date = models.DateField()
    chatroom_id = models.CharField(max_length=255)
    chatroom_name = models.TextField()
    word = models.CharField(max_length=255)
    number = models.IntegerField()
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'analysis_wx_chat_word'


class AnalysisWxChatroom(models.Model):
    chatroom_id = models.CharField(max_length=255)
    chatroom_name = models.TextField(blank=True, null=True)
    dt = models.DateField()
    data_type = models.IntegerField()
    enter_num = models.IntegerField()
    retreat_num = models.IntegerField()
    chatroom_num = models.IntegerField()
    account = models.FloatField(blank=True, null=True)
    activity_num = models.IntegerField()
    chat_record_num = models.IntegerField()
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'analysis_wx_chatroom'


class AnalysisWxChatroomV2(models.Model):
    dt = models.DateField()
    chatroom_id = models.CharField(max_length=255)
    chatroom_name = models.CharField(max_length=255)
    user_total_num = models.IntegerField()
    user_online_num = models.IntegerField()
    user_interact_text = models.TextField()
    user_interact_day_num = models.IntegerField()
    user_in_day_num = models.IntegerField()
    user_in_text = models.TextField()
    user_out_day_num = models.IntegerField()
    user_out_text = models.TextField()
    user_dive_day_num = models.IntegerField()
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'analysis_wx_chatroom_v2'


class AnalysisWxUser(models.Model):
    date = models.DateField()
    chatroom_id = models.CharField(max_length=255)
    chatroom_name = models.TextField(blank=True, null=True)
    user_id = models.CharField(max_length=255)
    user_name = models.TextField(blank=True, null=True)
    user_head = models.TextField()
    in_time = models.DateTimeField()
    out_time = models.DateTimeField(blank=True, null=True)
    in_period = models.IntegerField(blank=True, null=True)
    is_out = models.IntegerField()
    interact_num = models.IntegerField()
    interact_day_num = models.IntegerField()
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'analysis_wx_user'


class AsterGetdatajobLogBak(models.Model):
    jobname = models.CharField(db_column='jobName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='jobType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    handjobid = models.IntegerField(db_column='handJobId', blank=True, null=True)  # Field name made lowercase.
    handsubjobno = models.IntegerField(db_column='handSubJobNo', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    finishtime = models.DateTimeField(db_column='finishTime', blank=True, null=True)  # Field name made lowercase.
    effectnum = models.IntegerField(db_column='effectNum', blank=True, null=True)  # Field name made lowercase.
    pageno = models.IntegerField(db_column='pageNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_getDatajob_log_bak'


class AsterHandJob(models.Model):
    jobname = models.CharField(db_column='jobName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    subjobnum = models.IntegerField(db_column='subJobNum', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    finishtime = models.DateTimeField(db_column='finishTime', blank=True, null=True)  # Field name made lowercase.
    effectnum = models.IntegerField(db_column='effectNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_hand_job'


class AsterJobLog(models.Model):
    jobname = models.CharField(db_column='jobName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='jobType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    handjobid = models.IntegerField(db_column='handJobId', blank=True, null=True)  # Field name made lowercase.
    handsubjobno = models.IntegerField(db_column='handSubJobNo', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    finishtime = models.DateTimeField(db_column='finishTime', blank=True, null=True)  # Field name made lowercase.
    effectnum = models.IntegerField(db_column='effectNum', blank=True, null=True)  # Field name made lowercase.
    pageno = models.IntegerField(db_column='pageNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_job_log'


class AsterJobLogBak4D(models.Model):
    jobname = models.CharField(db_column='jobName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='jobType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    handjobid = models.IntegerField(db_column='handJobId', blank=True, null=True)  # Field name made lowercase.
    handsubjobno = models.IntegerField(db_column='handSubJobNo', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    finishtime = models.DateTimeField(db_column='finishTime', blank=True, null=True)  # Field name made lowercase.
    effectnum = models.IntegerField(db_column='effectNum', blank=True, null=True)  # Field name made lowercase.
    pageno = models.IntegerField(db_column='pageNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_job_log_bak_4d'


class AsterProperties(models.Model):
    name = models.CharField(unique=True, max_length=100)
    value = models.TextField(blank=True, null=True)
    propdesc = models.CharField(db_column='propDesc', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_properties'


class AsterSearchConditionGroup(models.Model):
    loginid = models.CharField(db_column='loginId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    searchname = models.CharField(db_column='searchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_search_condition_group'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class ChandleexcelStoragefilelocal(models.Model):
    id = models.IntegerField(blank=True,primary_key=True)
    excelfile = models.CharField(db_column='excelFile', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chandleexcel_storagefilelocal'


class CwAlipayOrder(models.Model):
    account_flow_num = models.CharField(max_length=255)
    business_flow_num = models.CharField(max_length=255, blank=True, null=True)
    merchant_order_num = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    occur_time = models.CharField(max_length=255, blank=True, null=True)
    other_account = models.CharField(max_length=255, blank=True, null=True)
    income_account = models.CharField(max_length=255, blank=True, null=True)
    payout_account = models.CharField(max_length=255, blank=True, null=True)
    balance_account = models.CharField(max_length=255, blank=True, null=True)
    trad_channel = models.CharField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    business_description = models.CharField(max_length=255, blank=True, null=True)
    business_bill_source = models.CharField(max_length=255, blank=True, null=True)
    tid = models.CharField(max_length=255, blank=True, null=True)
    business_order_num = models.CharField(max_length=255, blank=True, null=True)
    uploadtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cw_alipay_order'


class CwProductInfo(models.Model):
    product_detail_num = models.CharField(max_length=255, blank=True, null=True)
    product_code = models.CharField(max_length=255, blank=True, null=True)
    specification = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    brank = models.CharField(max_length=255, blank=True, null=True)
    product_classification = models.CharField(max_length=255, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    sale_cell_price = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    zmt_u8_code = models.CharField(max_length=255, blank=True, null=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    td_u8_code = models.CharField(max_length=255, blank=True, null=True)
    electronic_code = models.CharField(max_length=255, blank=True, null=True)
    yd_code = models.CharField(max_length=255, blank=True, null=True)
    xzt_code = models.CharField(max_length=255, blank=True, null=True)
    kmr_code = models.CharField(max_length=255, blank=True, null=True)
    ms_code = models.CharField(max_length=255, blank=True, null=True)
    ly_code = models.CharField(max_length=255, blank=True, null=True)
    yz_code = models.CharField(max_length=255, blank=True, null=True)
    hht_code = models.CharField(max_length=255, blank=True, null=True)
    zmt_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cw_product_info'


class CwSetBrandInfo(models.Model):
    set_brand = models.CharField(max_length=255, blank=True, null=True)
    set_brand_num = models.CharField(max_length=255, blank=True, null=True)
    specification = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    related_product_brands = models.CharField(max_length=255, blank=True, null=True)
    related_product_code = models.CharField(max_length=255, blank=True, null=True)
    related_product_specification = models.CharField(max_length=255, blank=True, null=True)
    related_product_barcode = models.CharField(max_length=255, blank=True, null=True)
    related_product_num = models.IntegerField(blank=True, null=True)
    related_product_name = models.CharField(max_length=255, blank=True, null=True)
    related_product_price = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cw_set_brand_info'


class CwWarehouseInfo(models.Model):
    warehouse_name = models.CharField(max_length=255)
    warehouse_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cw_warehouse_info'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
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


class DjceleryCrontabschedule(models.Model):
    minute = models.CharField(max_length=64)
    hour = models.CharField(max_length=64)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=64)
    month_of_year = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'djcelery_crontabschedule'


class DjceleryIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'djcelery_intervalschedule'


class DjceleryPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.PositiveIntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjceleryCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjceleryIntervalschedule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djcelery_periodictask'


class DjceleryPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'djcelery_periodictasks'


class DjceleryTaskstate(models.Model):
    state = models.CharField(max_length=64)
    task_id = models.CharField(unique=True, max_length=36)
    name = models.CharField(max_length=200, blank=True, null=True)
    tstamp = models.DateTimeField()
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    retries = models.IntegerField()
    hidden = models.IntegerField()
    worker = models.ForeignKey('DjceleryWorkerstate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djcelery_taskstate'


class DjceleryWorkerstate(models.Model):
    hostname = models.CharField(unique=True, max_length=255)
    last_heartbeat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djcelery_workerstate'


class JstOrderFullinfo(models.Model):
    tid = models.BigIntegerField(unique=True)
    tid_str = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    seller_nick = models.CharField(max_length=100, blank=True, null=True)
    buyer_nick = models.CharField(max_length=100, blank=True, null=True)
    created = models.CharField(max_length=30, blank=True, null=True)
    modified = models.CharField(max_length=30, blank=True, null=True)
    adjust_fee = models.CharField(max_length=20, blank=True, null=True)
    alipay_no = models.CharField(max_length=100, blank=True, null=True)
    alipay_point = models.CharField(max_length=20, blank=True, null=True)
    available_confirm_fee = models.CharField(max_length=100, blank=True, null=True)
    buyer_alipay_no = models.CharField(max_length=100, blank=True, null=True)
    buyer_area = models.CharField(max_length=100, blank=True, null=True)
    buyer_cod_fee = models.CharField(max_length=20, blank=True, null=True)
    buyer_email = models.CharField(max_length=100, blank=True, null=True)
    buyer_obtain_point_fee = models.CharField(max_length=20, blank=True, null=True)
    buyer_rate = models.CharField(max_length=10, blank=True, null=True)
    cod_fee = models.CharField(max_length=20, blank=True, null=True)
    cod_status = models.CharField(max_length=50, blank=True, null=True)
    commission_fee = models.CharField(max_length=20, blank=True, null=True)
    consign_time = models.CharField(max_length=30, blank=True, null=True)
    discount_fee = models.CharField(max_length=20, blank=True, null=True)
    has_post_fee = models.CharField(max_length=10, blank=True, null=True)
    is_3d = models.CharField(db_column='is_3D', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_brand_sale = models.CharField(max_length=10, blank=True, null=True)
    is_daixiao = models.CharField(max_length=10, blank=True, null=True)
    is_force_wlb = models.CharField(max_length=10, blank=True, null=True)
    is_sh_ship = models.CharField(max_length=10, blank=True, null=True)
    is_lgtype = models.CharField(max_length=10, blank=True, null=True)
    is_part_consign = models.CharField(max_length=10, blank=True, null=True)
    is_wt = models.CharField(max_length=10, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    num_iid = models.CharField(max_length=30, blank=True, null=True)
    pay_time = models.CharField(max_length=30, blank=True, null=True)
    payment = models.CharField(max_length=20, blank=True, null=True)
    pcc_af = models.CharField(max_length=20, blank=True, null=True)
    pic_path = models.CharField(max_length=200, blank=True, null=True)
    point_fee = models.CharField(max_length=20, blank=True, null=True)
    post_fee = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    real_point_fee = models.CharField(max_length=20, blank=True, null=True)
    received_payment = models.CharField(max_length=20, blank=True, null=True)
    receiver_address = models.CharField(max_length=200, blank=True, null=True)
    receiver_city = models.CharField(max_length=50, blank=True, null=True)
    receiver_district = models.CharField(max_length=50, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=20, blank=True, null=True)
    receiver_name = models.CharField(max_length=50, blank=True, null=True)
    receiver_phone = models.CharField(max_length=30, blank=True, null=True)
    receiver_state = models.CharField(max_length=100, blank=True, null=True)
    receiver_town = models.CharField(max_length=50, blank=True, null=True)
    receiver_zip = models.CharField(max_length=30, blank=True, null=True)
    seller_alipay_no = models.CharField(max_length=100, blank=True, null=True)
    seller_can_rate = models.CharField(max_length=10, blank=True, null=True)
    seller_cod_fee = models.CharField(max_length=20, blank=True, null=True)
    seller_email = models.CharField(max_length=50, blank=True, null=True)
    seller_flag = models.CharField(max_length=20, blank=True, null=True)
    seller_mobile = models.CharField(max_length=20, blank=True, null=True)
    seller_name = models.CharField(max_length=150, blank=True, null=True)
    seller_phone = models.CharField(max_length=20, blank=True, null=True)
    seller_rate = models.CharField(max_length=10, blank=True, null=True)
    send_time = models.CharField(max_length=30, blank=True, null=True)
    shipping_type = models.CharField(max_length=50, blank=True, null=True)
    snapshot_url = models.CharField(max_length=150, blank=True, null=True)
    step_paid_fee = models.CharField(max_length=20, blank=True, null=True)
    step_trade_status = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    total_fee = models.CharField(max_length=20, blank=True, null=True)
    trade_from = models.CharField(max_length=100, blank=True, null=True)
    end_time = models.CharField(max_length=30, blank=True, null=True)
    credit_card_fee = models.CharField(max_length=20, blank=True, null=True)
    buyer_message = models.TextField(blank=True, null=True)
    seller_memo = models.TextField(blank=True, null=True)
    trade_attr = models.TextField(blank=True, null=True)
    timeout_action_time = models.CharField(max_length=30, blank=True, null=True)
    ofp_hold = models.CharField(max_length=20, blank=True, null=True)
    delay_create_delivery = models.CharField(max_length=20, blank=True, null=True)
    buyer_ip = models.CharField(max_length=30, blank=True, null=True)
    alipay_id = models.CharField(max_length=50, blank=True, null=True)
    trade_source = models.CharField(max_length=100, blank=True, null=True)
    encrypt_alipay_id = models.CharField(max_length=100, blank=True, null=True)
    invoice_name = models.CharField(max_length=190, blank=True, null=True)
    express_agency_fee = models.CharField(max_length=20, blank=True, null=True)
    top_hold = models.CharField(max_length=50, blank=True, null=True)
    forbid_consign = models.CharField(max_length=50, blank=True, null=True)
    paid_coupon_fee = models.CharField(max_length=20, blank=True, null=True)
    jdp_created = models.CharField(max_length=30, blank=True, null=True)
    jdp_modified = models.CharField(max_length=30, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.CharField(db_column='updateTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jst_order_fullinfo'


class JstOrderFullinfoItem(models.Model):
    tid = models.BigIntegerField()
    tid_str = models.CharField(max_length=50, blank=True, null=True)
    seller_nick = models.CharField(max_length=100, blank=True, null=True)
    buyer_nick = models.CharField(max_length=100, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=20, blank=True, null=True)
    adjust_fee = models.CharField(max_length=20, blank=True, null=True)
    buyer_rate = models.CharField(max_length=10, blank=True, null=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    consign_time = models.CharField(max_length=30, blank=True, null=True)
    discount_fee = models.CharField(max_length=30, blank=True, null=True)
    divide_order_fee = models.CharField(max_length=30, blank=True, null=True)
    invoice_no = models.CharField(max_length=30, blank=True, null=True)
    is_daixiao = models.CharField(max_length=10, blank=True, null=True)
    is_oversold = models.CharField(max_length=10, blank=True, null=True)
    logistics_company = models.CharField(max_length=100, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    num_iid = models.CharField(max_length=30, blank=True, null=True)
    oid = models.BigIntegerField(unique=True, blank=True, null=True)
    oid_str = models.CharField(max_length=50, blank=True, null=True)
    order_from = models.CharField(max_length=50, blank=True, null=True)
    outer_sku_id = models.CharField(max_length=50, blank=True, null=True)
    part_mjz_discount = models.CharField(max_length=20, blank=True, null=True)
    payment = models.CharField(max_length=50, blank=True, null=True)
    pic_path = models.CharField(max_length=190, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    refund_status = models.CharField(max_length=50, blank=True, null=True)
    seller_rate = models.CharField(max_length=10, blank=True, null=True)
    seller_type = models.CharField(max_length=50, blank=True, null=True)
    shipping_type = models.CharField(max_length=50, blank=True, null=True)
    sku_id = models.CharField(max_length=100, blank=True, null=True)
    sku_properties_name = models.CharField(max_length=150, blank=True, null=True)
    snapshot_url = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=190, blank=True, null=True)
    total_fee = models.CharField(max_length=10, blank=True, null=True)
    outer_iid = models.CharField(max_length=50, blank=True, null=True)
    end_time = models.CharField(max_length=30, blank=True, null=True)
    refund_id = models.CharField(max_length=50, blank=True, null=True)
    timeout_action_time = models.CharField(max_length=30, blank=True, null=True)
    item_meal_id = models.CharField(max_length=50, blank=True, null=True)
    store_code = models.CharField(max_length=50, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.CharField(db_column='updateTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jst_order_fullinfo_item'


class JstOrderPromotionItem(models.Model):
    did = models.AutoField(primary_key=True)
    tid = models.BigIntegerField()
    tid_str = models.CharField(max_length=50, blank=True, null=True)
    firstlevelkey = models.CharField(db_column='firstLevelkey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    promotiontype = models.CharField(db_column='promotionType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    promotionbelongto = models.CharField(db_column='promotionBelongTo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discount_fee = models.CharField(max_length=20, blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    promotion_desc = models.CharField(max_length=150, blank=True, null=True)
    promotion_id = models.CharField(max_length=150, blank=True, null=True)
    promotion_name = models.CharField(max_length=100, blank=True, null=True)
    gift_item_name = models.CharField(max_length=180, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.CharField(db_column='updateTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jst_order_promotion_item'


class JstOrderServiceTagItem(models.Model):
    tid = models.BigIntegerField()
    firstlevelkey = models.CharField(db_column='firstLevelkey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_id = models.CharField(max_length=30, blank=True, null=True)
    secondlevelkey = models.CharField(db_column='secondLevelkey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    service_tag = models.CharField(max_length=1000, blank=True, null=True)
    service_type = models.CharField(max_length=150, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.CharField(db_column='updateTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jst_order_service_tag_item'


class JstShowData(models.Model):
    order_num = models.IntegerField()
    amount_total = models.FloatField()
    person_num = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jst_show_data'


class SEdbShop(models.Model):
    shopid = models.CharField(db_column='shopId', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    shopname = models.CharField(db_column='shopName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    platformtype = models.CharField(db_column='platformType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platformname = models.CharField(db_column='platformName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platformcode = models.CharField(db_column='platformCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isbigshop = models.IntegerField(db_column='isBigShop', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_edb_shop'


class SGroupInfo(models.Model):
    robot_id = models.CharField(max_length=255)
    chatroom_id = models.CharField(max_length=255)
    chatroom_name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_status = models.CharField(max_length=255)
    updatetime = models.DateTimeField()
    createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 's_group_info'


class SGroupMsg(models.Model):
    chatroom_name = models.CharField(max_length=255, blank=True, null=True)
    chatroom_id = models.IntegerField()
    user_id = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 's_group_msg'


class SGroupOutInfo(models.Model):
    community_id = models.CharField(max_length=255, blank=True, null=True)
    community_name = models.CharField(max_length=255, blank=True, null=True)
    chatroom_id = models.CharField(max_length=255)
    chatroom_name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 's_group_out_info'


class SOrder(models.Model):
    tid = models.CharField(unique=True, max_length=100, blank=True, null=True)
    masterid = models.CharField(db_column='masterId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsource = models.CharField(db_column='IDSource', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resultnum = models.CharField(db_column='resultNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    storage_id = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    distributor_id = models.CharField(max_length=100, blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    out_tid = models.CharField(max_length=100, blank=True, null=True)
    out_pay_tid = models.CharField(max_length=100, blank=True, null=True)
    voucher_id = models.CharField(max_length=100, blank=True, null=True)
    shopid = models.CharField(max_length=100, blank=True, null=True)
    serial_num = models.CharField(max_length=100, blank=True, null=True)
    order_channel = models.CharField(max_length=100, blank=True, null=True)
    order_from = models.CharField(max_length=100, blank=True, null=True)
    buyer_id = models.CharField(max_length=100, blank=True, null=True)
    buyer_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    abnormal_status = models.CharField(max_length=100, blank=True, null=True)
    merge_status = models.CharField(max_length=100, blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    is_bill = models.CharField(max_length=100, blank=True, null=True)
    invoice_name = models.CharField(max_length=100, blank=True, null=True)
    invoice_situation = models.CharField(max_length=100, blank=True, null=True)
    invoice_title = models.CharField(max_length=100, blank=True, null=True)
    invoice_type = models.CharField(max_length=100, blank=True, null=True)
    invoice_content = models.TextField(blank=True, null=True)
    pro_totalfee = models.CharField(max_length=100, blank=True, null=True)
    order_totalfee = models.CharField(max_length=100, blank=True, null=True)
    reference_price_paid = models.CharField(max_length=100, blank=True, null=True)
    invoice_fee = models.CharField(max_length=100, blank=True, null=True)
    cod_fee = models.CharField(max_length=100, blank=True, null=True)
    other_fee = models.CharField(max_length=100, blank=True, null=True)
    refund_totalfee = models.CharField(max_length=100, blank=True, null=True)
    discount_fee = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    channel_disfee = models.CharField(max_length=100, blank=True, null=True)
    merchant_disfee = models.CharField(max_length=100, blank=True, null=True)
    order_disfee = models.CharField(max_length=100, blank=True, null=True)
    commission_fee = models.CharField(max_length=100, blank=True, null=True)
    is_cod = models.CharField(max_length=100, blank=True, null=True)
    point_pay = models.CharField(max_length=100, blank=True, null=True)
    cost_point = models.CharField(max_length=100, blank=True, null=True)
    point = models.CharField(max_length=100, blank=True, null=True)
    superior_point = models.CharField(max_length=100, blank=True, null=True)
    royalty_fee = models.CharField(max_length=100, blank=True, null=True)
    external_point = models.CharField(max_length=100, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    express = models.CharField(max_length=100, blank=True, null=True)
    express_coding = models.CharField(max_length=100, blank=True, null=True)
    online_express = models.CharField(max_length=100, blank=True, null=True)
    sending_type = models.CharField(max_length=100, blank=True, null=True)
    real_income_freight = models.CharField(max_length=100, blank=True, null=True)
    real_pay_freight = models.CharField(max_length=100, blank=True, null=True)
    gross_weight = models.CharField(max_length=100, blank=True, null=True)
    gross_weight_freight = models.CharField(max_length=100, blank=True, null=True)
    net_weight_freight = models.CharField(max_length=100, blank=True, null=True)
    freight_explain = models.CharField(max_length=100, blank=True, null=True)
    total_weight = models.CharField(max_length=100, blank=True, null=True)
    tid_net_weight = models.CharField(max_length=100, blank=True, null=True)
    tid_time = models.CharField(max_length=100, blank=True, null=True)
    pay_time = models.CharField(max_length=100, blank=True, null=True)
    get_time = models.CharField(max_length=100, blank=True, null=True)
    order_creater = models.CharField(max_length=100, blank=True, null=True)
    business_man = models.CharField(max_length=100, blank=True, null=True)
    payment_received_operator = models.CharField(max_length=100, blank=True, null=True)
    payment_received_time = models.CharField(max_length=100, blank=True, null=True)
    review_orders_operator = models.CharField(max_length=100, blank=True, null=True)
    review_orders_time = models.CharField(max_length=100, blank=True, null=True)
    finance_review_operator = models.CharField(max_length=100, blank=True, null=True)
    finance_review_time = models.CharField(max_length=100, blank=True, null=True)
    advance_printer = models.CharField(max_length=100, blank=True, null=True)
    printer = models.CharField(max_length=100, blank=True, null=True)
    print_time = models.CharField(max_length=100, blank=True, null=True)
    is_print = models.CharField(max_length=100, blank=True, null=True)
    adv_distributer = models.CharField(max_length=100, blank=True, null=True)
    adv_distribut_time = models.CharField(max_length=100, blank=True, null=True)
    distributer = models.CharField(max_length=100, blank=True, null=True)
    distribut_time = models.CharField(max_length=100, blank=True, null=True)
    is_inspection = models.CharField(max_length=100, blank=True, null=True)
    inspecter = models.CharField(max_length=100, blank=True, null=True)
    inspect_time = models.CharField(max_length=100, blank=True, null=True)
    cancel_operator = models.CharField(max_length=100, blank=True, null=True)
    cancel_time = models.CharField(max_length=100, blank=True, null=True)
    revoke_cancel_er = models.CharField(max_length=100, blank=True, null=True)
    revoke_cancel_time = models.CharField(max_length=100, blank=True, null=True)
    packager = models.CharField(max_length=100, blank=True, null=True)
    pack_time = models.CharField(max_length=100, blank=True, null=True)
    weigh_operator = models.CharField(max_length=100, blank=True, null=True)
    weigh_time = models.CharField(max_length=100, blank=True, null=True)
    book_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    delivery_operator = models.CharField(max_length=100, blank=True, null=True)
    delivery_time = models.CharField(max_length=100, blank=True, null=True)
    locker = models.CharField(max_length=100, blank=True, null=True)
    lock_time = models.CharField(max_length=100, blank=True, null=True)
    book_file_time = models.CharField(max_length=100, blank=True, null=True)
    file_operator = models.CharField(max_length=100, blank=True, null=True)
    file_time = models.CharField(max_length=100, blank=True, null=True)
    finish_time = models.CharField(max_length=100, blank=True, null=True)
    modity_time = models.CharField(max_length=100, blank=True, null=True)
    is_promotion = models.CharField(max_length=100, blank=True, null=True)
    promotion_plan = models.TextField(blank=True, null=True)
    out_promotion_detail = models.TextField(blank=True, null=True)
    good_receive_time = models.CharField(max_length=100, blank=True, null=True)
    receive_time = models.CharField(max_length=100, blank=True, null=True)
    verificaty_time = models.CharField(max_length=100, blank=True, null=True)
    enable_inte_sto_time = models.CharField(max_length=100, blank=True, null=True)
    enable_inte_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    alipay_id = models.CharField(max_length=100, blank=True, null=True)
    alipay_status = models.CharField(max_length=100, blank=True, null=True)
    pay_mothed = models.CharField(max_length=100, blank=True, null=True)
    pay_status = models.CharField(max_length=100, blank=True, null=True)
    platform_status = models.CharField(max_length=100, blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=100, blank=True, null=True)
    delivery_status = models.CharField(max_length=100, blank=True, null=True)
    buyer_message = models.TextField(blank=True, null=True)
    service_remarks = models.TextField(blank=True, null=True)
    inner_lable = models.TextField(blank=True, null=True)
    distributor_mark = models.TextField(blank=True, null=True)
    system_remarks = models.TextField(blank=True, null=True)
    other_remarks = models.TextField(blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    message_time = models.CharField(max_length=100, blank=True, null=True)
    is_stock = models.CharField(max_length=100, blank=True, null=True)
    related_orders = models.CharField(max_length=500, blank=True, null=True)
    related_orders_type = models.CharField(max_length=100, blank=True, null=True)
    import_mark = models.CharField(max_length=100, blank=True, null=True)
    delivery_name = models.CharField(max_length=100, blank=True, null=True)
    is_new_customer = models.CharField(max_length=100, blank=True, null=True)
    distributor_level = models.CharField(max_length=100, blank=True, null=True)
    cod_service_fee = models.CharField(max_length=100, blank=True, null=True)
    express_col_fee = models.CharField(max_length=100, blank=True, null=True)
    product_num = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    item_num = models.CharField(max_length=100, blank=True, null=True)
    single_num = models.CharField(max_length=100, blank=True, null=True)
    flag_color = models.CharField(max_length=100, blank=True, null=True)
    is_flag = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_order_status = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_status = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_method = models.CharField(max_length=100, blank=True, null=True)
    order_process_time = models.CharField(max_length=100, blank=True, null=True)
    is_break = models.CharField(max_length=100, blank=True, null=True)
    breaker = models.CharField(max_length=100, blank=True, null=True)
    break_time = models.CharField(max_length=100, blank=True, null=True)
    break_explain = models.CharField(max_length=1000, blank=True, null=True)
    plat_send_status = models.CharField(max_length=100, blank=True, null=True)
    plat_type = models.CharField(max_length=100, blank=True, null=True)
    is_adv_sale = models.CharField(max_length=100, blank=True, null=True)
    provinc_code = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=100, blank=True, null=True)
    area_code = models.CharField(max_length=100, blank=True, null=True)
    express_code = models.CharField(max_length=100, blank=True, null=True)
    last_returned_time = models.CharField(max_length=100, blank=True, null=True)
    last_refund_time = models.CharField(max_length=100, blank=True, null=True)
    deliver_centre = models.CharField(max_length=100, blank=True, null=True)
    deliver_station = models.CharField(max_length=100, blank=True, null=True)
    is_pre_delivery_notice = models.CharField(max_length=100, blank=True, null=True)
    jd_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    sorting_code = models.CharField(db_column='Sorting_code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_settlement_vouchernumber = models.CharField(max_length=100, blank=True, null=True)
    three_codes = models.CharField(max_length=100, blank=True, null=True)
    send_site_name = models.CharField(max_length=100, blank=True, null=True)
    distributing_centre_name = models.CharField(max_length=100, blank=True, null=True)
    origincode = models.CharField(db_column='originCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    destcode = models.CharField(db_column='destCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    big_marker = models.CharField(max_length=100, blank=True, null=True)
    platform_preferential = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's_order'


class SOrderItem(models.Model):
    tid = models.CharField(max_length=100, blank=True, null=True)
    pro_detail_code = models.CharField(max_length=20, blank=True, null=True)
    pro_name = models.CharField(max_length=150, blank=True, null=True)
    specification = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    combine_barcode = models.CharField(max_length=100, blank=True, null=True)
    iscancel = models.CharField(max_length=100, blank=True, null=True)
    isscheduled = models.CharField(max_length=100, blank=True, null=True)
    stock_situation = models.TextField(blank=True, null=True)
    isbook_pro = models.CharField(max_length=100, blank=True, null=True)
    iscombination = models.CharField(max_length=100, blank=True, null=True)
    isgifts = models.CharField(max_length=100, blank=True, null=True)
    gift_num = models.IntegerField(blank=True, null=True)
    book_storage = models.CharField(max_length=100, blank=True, null=True)
    pro_num = models.IntegerField(blank=True, null=True)
    send_num = models.IntegerField(blank=True, null=True)
    refund_num = models.IntegerField(blank=True, null=True)
    refund_renum = models.IntegerField(blank=True, null=True)
    inspection_num = models.IntegerField(blank=True, null=True)
    timeinventory = models.CharField(max_length=100, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sell_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    average_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    original_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sys_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ferght = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_discountfee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    inspection_time = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    shopid = models.CharField(max_length=100, blank=True, null=True)
    out_tid = models.CharField(max_length=100, blank=True, null=True)
    out_proid = models.CharField(max_length=100, blank=True, null=True)
    out_prosku = models.CharField(max_length=100, blank=True, null=True)
    proexplain = models.TextField(blank=True, null=True)
    buyer_memo = models.TextField(blank=True, null=True)
    seller_remark = models.TextField(blank=True, null=True)
    distributer = models.CharField(max_length=100, blank=True, null=True)
    distribut_time = models.CharField(max_length=100, blank=True, null=True)
    second_barcode = models.CharField(max_length=100, blank=True, null=True)
    product_no = models.CharField(max_length=100, blank=True, null=True)
    brand_number = models.CharField(max_length=100, blank=True, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    book_inventory = models.CharField(max_length=100, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    md5_encryption = models.CharField(db_column='MD5_encryption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sncode = models.CharField(max_length=100, blank=True, null=True)
    store_location = models.CharField(max_length=500, blank=True, null=True)
    pro_type = models.CharField(max_length=100, blank=True, null=True)
    storage_id = models.CharField(max_length=100, blank=True, null=True)
    credit_amount = models.CharField(max_length=100, blank=True, null=True)
    masterid = models.CharField(db_column='masterID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsource = models.CharField(db_column='IDSource', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_specification = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's_order_item'


class SOrderItemOld0516(models.Model):
    tid = models.CharField(max_length=100, blank=True, null=True)
    pro_detail_code = models.CharField(max_length=20, blank=True, null=True)
    pro_name = models.CharField(max_length=100, blank=True, null=True)
    specification = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    combine_barcode = models.CharField(max_length=100, blank=True, null=True)
    iscancel = models.CharField(max_length=100, blank=True, null=True)
    isscheduled = models.CharField(max_length=100, blank=True, null=True)
    stock_situation = models.CharField(max_length=100, blank=True, null=True)
    isbook_pro = models.CharField(max_length=100, blank=True, null=True)
    iscombination = models.CharField(max_length=100, blank=True, null=True)
    isgifts = models.CharField(max_length=100, blank=True, null=True)
    gift_num = models.IntegerField(blank=True, null=True)
    book_storage = models.CharField(max_length=100, blank=True, null=True)
    pro_num = models.IntegerField(blank=True, null=True)
    send_num = models.IntegerField(blank=True, null=True)
    refund_num = models.IntegerField(blank=True, null=True)
    refund_renum = models.IntegerField(blank=True, null=True)
    inspection_num = models.IntegerField(blank=True, null=True)
    timeinventory = models.CharField(max_length=100, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sell_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    average_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    original_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sys_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    ferght = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    item_discountfee = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    inspection_time = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    shopid = models.CharField(max_length=100, blank=True, null=True)
    out_tid = models.CharField(max_length=100, blank=True, null=True)
    out_proid = models.CharField(max_length=100, blank=True, null=True)
    out_prosku = models.CharField(max_length=100, blank=True, null=True)
    proexplain = models.CharField(max_length=100, blank=True, null=True)
    buyer_memo = models.CharField(max_length=1000, blank=True, null=True)
    seller_remark = models.CharField(max_length=1000, blank=True, null=True)
    distributer = models.CharField(max_length=100, blank=True, null=True)
    distribut_time = models.CharField(max_length=100, blank=True, null=True)
    second_barcode = models.CharField(max_length=100, blank=True, null=True)
    product_no = models.CharField(max_length=100, blank=True, null=True)
    brand_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    book_inventory = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    md5_encryption = models.CharField(db_column='MD5_encryption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sncode = models.CharField(max_length=100, blank=True, null=True)
    store_location = models.CharField(max_length=100, blank=True, null=True)
    pro_type = models.CharField(max_length=100, blank=True, null=True)
    storage_id = models.CharField(max_length=100, blank=True, null=True)
    credit_amount = models.CharField(max_length=100, blank=True, null=True)
    masterid = models.CharField(db_column='masterID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsource = models.CharField(db_column='IDSource', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_specification = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's_order_item_old_0516'


class SOrderOld0516(models.Model):
    tid = models.CharField(unique=True, max_length=100, blank=True, null=True)
    masterid = models.CharField(db_column='masterId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsource = models.CharField(db_column='IDSource', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resultnum = models.CharField(db_column='resultNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    storage_id = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    distributor_id = models.CharField(max_length=100, blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    out_tid = models.CharField(max_length=100, blank=True, null=True)
    out_pay_tid = models.CharField(max_length=100, blank=True, null=True)
    voucher_id = models.CharField(max_length=100, blank=True, null=True)
    shopid = models.CharField(max_length=100, blank=True, null=True)
    serial_num = models.CharField(max_length=100, blank=True, null=True)
    order_channel = models.CharField(max_length=100, blank=True, null=True)
    order_from = models.CharField(max_length=100, blank=True, null=True)
    buyer_id = models.CharField(max_length=100, blank=True, null=True)
    buyer_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    abnormal_status = models.CharField(max_length=100, blank=True, null=True)
    merge_status = models.CharField(max_length=100, blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    is_bill = models.CharField(max_length=100, blank=True, null=True)
    invoice_name = models.CharField(max_length=100, blank=True, null=True)
    invoice_situation = models.CharField(max_length=100, blank=True, null=True)
    invoice_title = models.CharField(max_length=100, blank=True, null=True)
    invoice_type = models.CharField(max_length=100, blank=True, null=True)
    invoice_content = models.CharField(max_length=100, blank=True, null=True)
    pro_totalfee = models.CharField(max_length=100, blank=True, null=True)
    order_totalfee = models.CharField(max_length=100, blank=True, null=True)
    reference_price_paid = models.CharField(max_length=100, blank=True, null=True)
    invoice_fee = models.CharField(max_length=100, blank=True, null=True)
    cod_fee = models.CharField(max_length=100, blank=True, null=True)
    other_fee = models.CharField(max_length=100, blank=True, null=True)
    refund_totalfee = models.CharField(max_length=100, blank=True, null=True)
    discount_fee = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    channel_disfee = models.CharField(max_length=100, blank=True, null=True)
    merchant_disfee = models.CharField(max_length=100, blank=True, null=True)
    order_disfee = models.CharField(max_length=100, blank=True, null=True)
    commission_fee = models.CharField(max_length=100, blank=True, null=True)
    is_cod = models.CharField(max_length=100, blank=True, null=True)
    point_pay = models.CharField(max_length=100, blank=True, null=True)
    cost_point = models.CharField(max_length=100, blank=True, null=True)
    point = models.CharField(max_length=100, blank=True, null=True)
    superior_point = models.CharField(max_length=100, blank=True, null=True)
    royalty_fee = models.CharField(max_length=100, blank=True, null=True)
    external_point = models.CharField(max_length=100, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    express = models.CharField(max_length=100, blank=True, null=True)
    express_coding = models.CharField(max_length=100, blank=True, null=True)
    online_express = models.CharField(max_length=100, blank=True, null=True)
    sending_type = models.CharField(max_length=100, blank=True, null=True)
    real_income_freight = models.CharField(max_length=100, blank=True, null=True)
    real_pay_freight = models.CharField(max_length=100, blank=True, null=True)
    gross_weight = models.CharField(max_length=100, blank=True, null=True)
    gross_weight_freight = models.CharField(max_length=100, blank=True, null=True)
    net_weight_freight = models.CharField(max_length=100, blank=True, null=True)
    freight_explain = models.CharField(max_length=100, blank=True, null=True)
    total_weight = models.CharField(max_length=100, blank=True, null=True)
    tid_net_weight = models.CharField(max_length=100, blank=True, null=True)
    tid_time = models.CharField(max_length=100, blank=True, null=True)
    pay_time = models.CharField(max_length=100, blank=True, null=True)
    get_time = models.CharField(max_length=100, blank=True, null=True)
    order_creater = models.CharField(max_length=100, blank=True, null=True)
    business_man = models.CharField(max_length=100, blank=True, null=True)
    payment_received_operator = models.CharField(max_length=100, blank=True, null=True)
    payment_received_time = models.CharField(max_length=100, blank=True, null=True)
    review_orders_operator = models.CharField(max_length=100, blank=True, null=True)
    review_orders_time = models.CharField(max_length=100, blank=True, null=True)
    finance_review_operator = models.CharField(max_length=100, blank=True, null=True)
    finance_review_time = models.CharField(max_length=100, blank=True, null=True)
    advance_printer = models.CharField(max_length=100, blank=True, null=True)
    printer = models.CharField(max_length=100, blank=True, null=True)
    print_time = models.CharField(max_length=100, blank=True, null=True)
    is_print = models.CharField(max_length=100, blank=True, null=True)
    adv_distributer = models.CharField(max_length=100, blank=True, null=True)
    adv_distribut_time = models.CharField(max_length=100, blank=True, null=True)
    distributer = models.CharField(max_length=100, blank=True, null=True)
    distribut_time = models.CharField(max_length=100, blank=True, null=True)
    is_inspection = models.CharField(max_length=100, blank=True, null=True)
    inspecter = models.CharField(max_length=100, blank=True, null=True)
    inspect_time = models.CharField(max_length=100, blank=True, null=True)
    cancel_operator = models.CharField(max_length=100, blank=True, null=True)
    cancel_time = models.CharField(max_length=100, blank=True, null=True)
    revoke_cancel_er = models.CharField(max_length=100, blank=True, null=True)
    revoke_cancel_time = models.CharField(max_length=100, blank=True, null=True)
    packager = models.CharField(max_length=100, blank=True, null=True)
    pack_time = models.CharField(max_length=100, blank=True, null=True)
    weigh_operator = models.CharField(max_length=100, blank=True, null=True)
    weigh_time = models.CharField(max_length=100, blank=True, null=True)
    book_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    delivery_operator = models.CharField(max_length=100, blank=True, null=True)
    delivery_time = models.CharField(max_length=100, blank=True, null=True)
    locker = models.CharField(max_length=100, blank=True, null=True)
    lock_time = models.CharField(max_length=100, blank=True, null=True)
    book_file_time = models.CharField(max_length=100, blank=True, null=True)
    file_operator = models.CharField(max_length=100, blank=True, null=True)
    file_time = models.CharField(max_length=100, blank=True, null=True)
    finish_time = models.CharField(max_length=100, blank=True, null=True)
    modity_time = models.CharField(max_length=100, blank=True, null=True)
    is_promotion = models.CharField(max_length=100, blank=True, null=True)
    promotion_plan = models.TextField(blank=True, null=True)
    out_promotion_detail = models.CharField(max_length=100, blank=True, null=True)
    good_receive_time = models.CharField(max_length=100, blank=True, null=True)
    receive_time = models.CharField(max_length=100, blank=True, null=True)
    verificaty_time = models.CharField(max_length=100, blank=True, null=True)
    enable_inte_sto_time = models.CharField(max_length=100, blank=True, null=True)
    enable_inte_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    alipay_id = models.CharField(max_length=100, blank=True, null=True)
    alipay_status = models.CharField(max_length=100, blank=True, null=True)
    pay_mothed = models.CharField(max_length=100, blank=True, null=True)
    pay_status = models.CharField(max_length=100, blank=True, null=True)
    platform_status = models.CharField(max_length=100, blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=100, blank=True, null=True)
    delivery_status = models.CharField(max_length=100, blank=True, null=True)
    buyer_message = models.CharField(max_length=300, blank=True, null=True)
    service_remarks = models.CharField(max_length=1500, blank=True, null=True)
    inner_lable = models.CharField(max_length=300, blank=True, null=True)
    distributor_mark = models.TextField(blank=True, null=True)
    system_remarks = models.TextField(blank=True, null=True)
    other_remarks = models.TextField(blank=True, null=True)
    message = models.CharField(max_length=100, blank=True, null=True)
    message_time = models.CharField(max_length=100, blank=True, null=True)
    is_stock = models.CharField(max_length=100, blank=True, null=True)
    related_orders = models.CharField(max_length=100, blank=True, null=True)
    related_orders_type = models.CharField(max_length=100, blank=True, null=True)
    import_mark = models.CharField(max_length=100, blank=True, null=True)
    delivery_name = models.CharField(max_length=100, blank=True, null=True)
    is_new_customer = models.CharField(max_length=100, blank=True, null=True)
    distributor_level = models.CharField(max_length=100, blank=True, null=True)
    cod_service_fee = models.CharField(max_length=100, blank=True, null=True)
    express_col_fee = models.CharField(max_length=100, blank=True, null=True)
    product_num = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    item_num = models.CharField(max_length=100, blank=True, null=True)
    single_num = models.CharField(max_length=100, blank=True, null=True)
    flag_color = models.CharField(max_length=100, blank=True, null=True)
    is_flag = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_order_status = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_status = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_method = models.CharField(max_length=100, blank=True, null=True)
    order_process_time = models.CharField(max_length=100, blank=True, null=True)
    is_break = models.CharField(max_length=100, blank=True, null=True)
    breaker = models.CharField(max_length=100, blank=True, null=True)
    break_time = models.CharField(max_length=100, blank=True, null=True)
    break_explain = models.CharField(max_length=200, blank=True, null=True)
    plat_send_status = models.CharField(max_length=100, blank=True, null=True)
    plat_type = models.CharField(max_length=100, blank=True, null=True)
    is_adv_sale = models.CharField(max_length=100, blank=True, null=True)
    provinc_code = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=100, blank=True, null=True)
    area_code = models.CharField(max_length=100, blank=True, null=True)
    express_code = models.CharField(max_length=100, blank=True, null=True)
    last_returned_time = models.CharField(max_length=100, blank=True, null=True)
    last_refund_time = models.CharField(max_length=100, blank=True, null=True)
    deliver_centre = models.CharField(max_length=100, blank=True, null=True)
    deliver_station = models.CharField(max_length=100, blank=True, null=True)
    is_pre_delivery_notice = models.CharField(max_length=100, blank=True, null=True)
    jd_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    sorting_code = models.CharField(db_column='Sorting_code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_settlement_vouchernumber = models.CharField(max_length=100, blank=True, null=True)
    three_codes = models.CharField(max_length=100, blank=True, null=True)
    send_site_name = models.CharField(max_length=100, blank=True, null=True)
    distributing_centre_name = models.CharField(max_length=100, blank=True, null=True)
    origincode = models.CharField(db_column='originCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    destcode = models.CharField(db_column='destCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    big_marker = models.CharField(max_length=100, blank=True, null=True)
    platform_preferential = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's_order_old_0516'


class SyncTableDataCheck(models.Model):
    check_table_tag_name = models.CharField(max_length=120, blank=True, null=True)
    start_id = models.BigIntegerField(blank=True, null=True)
    page_size = models.IntegerField(blank=True, null=True)
    data_count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_table_data_check'


class UUser(models.Model):
    userid = models.BigIntegerField(db_column='userId', unique=True, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(unique=True, max_length=50, blank=True, null=True)
    aliwangwang = models.CharField(unique=True, max_length=100, blank=True, null=True)
    wechatid = models.CharField(db_column='wechatId', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    zimeihuiuserid = models.CharField(db_column='zimeihuiUserId', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    headimgurl = models.TextField(db_column='headImgurl', blank=True, null=True)  # Field name made lowercase.
    shendenguid = models.CharField(db_column='shendengUid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(max_length=100, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    birthyear = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    province = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=200, blank=True, null=True)
    chatcount = models.IntegerField(db_column='chatCount', blank=True, null=True)  # Field name made lowercase.
    firstchattime = models.DateTimeField(db_column='firstChatTime', blank=True, null=True)  # Field name made lowercase.
    firstchatplatform = models.CharField(db_column='firstChatPlatform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstchatwith = models.CharField(db_column='firstChatWith', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchattime = models.DateTimeField(db_column='lastChatTime', blank=True, null=True)  # Field name made lowercase.
    lastchatplatform = models.CharField(db_column='lastChatPlatform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchatwith = models.CharField(db_column='lastChatWith', max_length=50, blank=True, null=True)  # Field name made lowercase.
    payamount = models.FloatField(db_column='payAmount', blank=True, null=True)  # Field name made lowercase.
    paycount = models.IntegerField(db_column='payCount', blank=True, null=True)  # Field name made lowercase.
    refundamount = models.FloatField(db_column='refundAmount', blank=True, null=True)  # Field name made lowercase.
    refundcount = models.IntegerField(db_column='refundCount', blank=True, null=True)  # Field name made lowercase.
    lastpayamount = models.FloatField(db_column='lastPayAmount', blank=True, null=True)  # Field name made lowercase.
    lastpaytime = models.DateTimeField(db_column='lastPayTime', blank=True, null=True)  # Field name made lowercase.
    firstpayamount = models.FloatField(db_column='firstPayAmount', blank=True, null=True)  # Field name made lowercase.
    firstpaytime = models.DateTimeField(db_column='firstPayTime', blank=True, null=True)  # Field name made lowercase.
    firstlogintime = models.DateTimeField(db_column='firstLoginTime', blank=True, null=True)  # Field name made lowercase.
    firstloginplatform = models.CharField(db_column='firstLoginPlatform', max_length=100, blank=True, null=True)  # Field name made lowercase.
    istaobaouser = models.IntegerField(db_column='isTaobaoUser', blank=True, null=True)  # Field name made lowercase.
    iswechatuser = models.IntegerField(db_column='isWechatUser', blank=True, null=True)  # Field name made lowercase.
    iszimeihuiuser = models.IntegerField(db_column='isZimeihuiUser', blank=True, null=True)  # Field name made lowercase.
    istaobaochated = models.IntegerField(db_column='isTaobaoChated', blank=True, null=True)  # Field name made lowercase.
    iswechatchated = models.IntegerField(db_column='isWechatChated', blank=True, null=True)  # Field name made lowercase.
    iszimeihuichated = models.IntegerField(db_column='isZimeihuiChated', blank=True, null=True)  # Field name made lowercase.
    istaobaopayed = models.IntegerField(db_column='isTaobaoPayed', blank=True, null=True)  # Field name made lowercase.
    iswechatpayed = models.IntegerField(db_column='isWechatPayed', blank=True, null=True)  # Field name made lowercase.
    iszimeihuipayed = models.IntegerField(db_column='isZimeihuiPayed', blank=True, null=True)  # Field name made lowercase.
    taobaopayamount = models.FloatField(db_column='taobaoPayAmount', blank=True, null=True)  # Field name made lowercase.
    taobaopaycount = models.IntegerField(db_column='taobaoPayCount', blank=True, null=True)  # Field name made lowercase.
    taobaofirstpayamount = models.FloatField(db_column='taobaoFirstPayAmount', blank=True, null=True)  # Field name made lowercase.
    taobaofirstpaytime = models.IntegerField(db_column='taobaoFirstPayTime', blank=True, null=True)  # Field name made lowercase.
    taobaolastpayamount = models.FloatField(db_column='taobaoLastPayAmount', blank=True, null=True)  # Field name made lowercase.
    taobaolastpaytime = models.DateTimeField(db_column='taobaoLastPayTime', blank=True, null=True)  # Field name made lowercase.
    wechatchatcout = models.IntegerField(db_column='wechatChatCout', blank=True, null=True)  # Field name made lowercase.
    wechatchatinfototal = models.IntegerField(db_column='wechatChatInfoTotal', blank=True, null=True)  # Field name made lowercase.
    wechatno = models.CharField(db_column='wechatNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatnickname = models.CharField(db_column='wechatNickname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatbelongto = models.TextField(db_column='wechatBelongTo', blank=True, null=True)  # Field name made lowercase.
    wechatfirstadd = models.CharField(db_column='wechatFirstAdd', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatfirstaddtime = models.DateTimeField(db_column='wechatFirstAddTime', blank=True, null=True)  # Field name made lowercase.
    wechatfirstchatwith = models.CharField(db_column='wechatFirstChatWith', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatfirstchattime = models.DateTimeField(db_column='wechatFirstChatTime', blank=True, null=True)  # Field name made lowercase.
    wechatlastchatwith = models.CharField(db_column='wechatLastChatWith', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatlastchattime = models.DateTimeField(db_column='wechatLastChatTime', blank=True, null=True)  # Field name made lowercase.
    wechatpayamount = models.FloatField(db_column='wechatPayAmount', blank=True, null=True)  # Field name made lowercase.
    wechatpaycount = models.IntegerField(db_column='wechatPayCount', blank=True, null=True)  # Field name made lowercase.
    wechatfirstpaytime = models.DateTimeField(db_column='wechatFirstPayTime', blank=True, null=True)  # Field name made lowercase.
    wecahtfirstpayamount = models.FloatField(db_column='wecahtFirstPayAmount', blank=True, null=True)  # Field name made lowercase.
    wecahtlastpaytime = models.DateTimeField(db_column='wecahtLastPayTime', blank=True, null=True)  # Field name made lowercase.
    wechatlastpayamount = models.FloatField(db_column='wechatLastPayAmount', blank=True, null=True)  # Field name made lowercase.
    wechatlifestatus = models.CharField(db_column='wechatLifeStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wechatisvipcarduser = models.IntegerField(db_column='wechatIsVIPCardUser', blank=True, null=True)  # Field name made lowercase.
    wechatviptime = models.DateTimeField(db_column='wechatVIPTime', blank=True, null=True)  # Field name made lowercase.
    wechatvipcardbalance = models.FloatField(db_column='wechatVIPCardBalance', blank=True, null=True)  # Field name made lowercase.
    wechatvipcardamount = models.FloatField(db_column='wechatVIPCardAmount', blank=True, null=True)  # Field name made lowercase.
    zimeihuiphone = models.CharField(db_column='zimeihuiPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zimeihuinickname = models.CharField(db_column='zimeihuiNickname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    zimeihuifxrole = models.CharField(db_column='zimeihuiFXRole', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zimeihuiregistertime = models.DateTimeField(db_column='zimeihuiRegisterTime', blank=True, null=True)  # Field name made lowercase.
    zimeihuifirstpaytime = models.DateTimeField(db_column='zimeihuiFirstPayTime', blank=True, null=True)  # Field name made lowercase.
    zimeihuifirstpayamount = models.FloatField(db_column='zimeihuiFirstPayAmount', blank=True, null=True)  # Field name made lowercase.
    zimeihuilastpaytime = models.DateTimeField(db_column='zimeihuiLastPayTime', blank=True, null=True)  # Field name made lowercase.
    zimeihuipayamount = models.FloatField(db_column='zimeihuiPayAmount', blank=True, null=True)  # Field name made lowercase.
    zimeihuipaycount = models.IntegerField(db_column='zimeihuiPayCount', blank=True, null=True)  # Field name made lowercase.
    iswoaregister = models.IntegerField(db_column='isWOARegister', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createsource = models.CharField(db_column='createSource', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user'


class UUserBasicInfoRecord(models.Model):
    userid = models.CharField(db_column='userId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=50, blank=True, null=True)
    sourceid = models.CharField(db_column='sourceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headimgurl = models.CharField(db_column='headImgurl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(blank=True, null=True)
    birthday = models.CharField(max_length=20, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user_basic_info_record'


class UUserConflict(models.Model):
    userid = models.BigIntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    userid2 = models.BigIntegerField(db_column='userId2', blank=True, null=True)  # Field name made lowercase.
    conflicttime = models.DateTimeField(db_column='conflictTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    ismerged = models.IntegerField(db_column='isMerged', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user_conflict'


class UUserMachineTags(models.Model):
    u_user_id = models.IntegerField()
    chat_words_clound_pic = models.CharField(max_length=100, blank=True, null=True)
    chat_words_clound_content = models.TextField(blank=True, null=True)
    cwcc_update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    extra_infos = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user_machine_tags'


class UUserTag(models.Model):
    userid = models.BigIntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='tagName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tagtype = models.CharField(db_column='tagType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firstcategoryid = models.IntegerField(db_column='firstCategoryId', blank=True, null=True)  # Field name made lowercase.
    uidvalue = models.CharField(db_column='uidValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uidtype = models.CharField(db_column='uidType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tagsrc = models.CharField(db_column='tagSrc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tagdetaillink = models.CharField(db_column='tagDetailLink', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user_tag'
        unique_together = (('userid', 'tagname', 'categoryname'),)


class WangwangMessages(models.Model):
    employee_code = models.CharField(max_length=100, blank=True, null=True)
    customer_code = models.CharField(max_length=100, blank=True, null=True)
    is_employee = models.PositiveIntegerField(blank=True, null=True)
    msg_content = models.TextField(blank=True, null=True)
    msg_timer = models.DateTimeField()
    hash_code = models.CharField(max_length=32, blank=True, null=True)
    etl_flag = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wangwang_messages'


class WxMsgSendEmployeeInfos(models.Model):
    wechat_no = models.CharField(primary_key=True, max_length=60)
    employee_id = models.PositiveIntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=20, blank=True, null=True)
    group_id = models.PositiveIntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=50, blank=True, null=True)
    team_id = models.PositiveIntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=50, blank=True, null=True)
    business_type = models.CharField(max_length=20, blank=True, null=True)
    extra = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wx_msg_send_employee_infos'


class WxMsgSendLogger(models.Model):
    wx_touserid = models.CharField(max_length=150, blank=True, null=True)
    wechat_no = models.CharField(max_length=60, blank=True, null=True)
    uuser_id = models.CharField(max_length=60, blank=True, null=True)
    msg_type = models.PositiveIntegerField(blank=True, null=True)
    msg_title = models.CharField(max_length=100, blank=True, null=True)
    msg_link = models.CharField(max_length=200, blank=True, null=True)
    msg_content = models.CharField(max_length=500, blank=True, null=True)
    msg_status = models.PositiveIntegerField(blank=True, null=True)
    case_rule_name = models.CharField(max_length=50, blank=True, null=True)
    success_time = models.DateTimeField(blank=True, null=True)
    success_time_str = models.CharField(max_length=10, blank=True, null=True)
    send_content = models.TextField(blank=True, null=True)
    send_md5 = models.CharField(max_length=32, blank=True, null=True)
    pulish_code = models.CharField(max_length=150, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    extra = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wx_msg_send_logger'


class WxMsgSenderTempCount(models.Model):
    success_time_str = models.CharField(primary_key=True, max_length=10)
    wechat_no = models.CharField(max_length=60)
    success_times = models.PositiveIntegerField(blank=True, null=True)
    last_success_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wx_msg_sender_temp_count'
        unique_together = (('success_time_str', 'wechat_no'),)


class WxUserChatrooms(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    chatroom_username = models.CharField(max_length=120, blank=True, null=True)
    parent_wx_userid = models.CharField(max_length=120, blank=True, null=True)
    parent_wx_nickname = models.CharField(max_length=100, blank=True, null=True)
    wx_userid = models.CharField(max_length=120, blank=True, null=True)
    wx_nickname = models.CharField(max_length=100, blank=True, null=True)
    parentid = models.PositiveIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.BigIntegerField(blank=True, null=True)
    updatetime = models.BigIntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    wx_headimg = models.CharField(max_length=255, blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    wx_number = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'wx_user_chatrooms'
        unique_together = (('id', 'wx_number'), ('chatroom_username', 'wx_userid'),)


class WxUserInfos(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    wx_userid = models.CharField(max_length=150)
    wx_alisa = models.CharField(max_length=100, blank=True, null=True)
    wx_truename = models.CharField(max_length=45, blank=True, null=True)
    wx_headid = models.CharField(max_length=300, blank=True, null=True)
    wx_mobile = models.CharField(max_length=45, blank=True, null=True)
    wx_nickname = models.CharField(max_length=200, blank=True, null=True)
    wx_signature = models.CharField(max_length=200, blank=True, null=True)
    wx_remark = models.CharField(max_length=200, blank=True, null=True)
    wx_guestid = models.CharField(max_length=45, blank=True, null=True)
    wx_flag = models.PositiveIntegerField(blank=True, null=True)
    wx_createtime = models.BigIntegerField(blank=True, null=True)
    wx_updatetime = models.BigIntegerField(blank=True, null=True)
    wx_deltime = models.BigIntegerField(blank=True, null=True)
    wx_type = models.PositiveIntegerField(blank=True, null=True)
    wx_verifyflag = models.PositiveIntegerField(db_column='wx_verifyFlag', blank=True, null=True)  # Field name made lowercase.
    wx_usertype = models.CharField(max_length=45, blank=True, null=True)
    wx_pinyin_full = models.CharField(max_length=100, blank=True, null=True)
    wx_pinyin_first = models.CharField(max_length=45, blank=True, null=True)
    wx_time_fix = models.PositiveSmallIntegerField(blank=True, null=True)
    wx_labels = models.TextField(blank=True, null=True)
    wx_free1 = models.CharField(max_length=45, blank=True, null=True)
    wx_free2 = models.CharField(max_length=45, blank=True, null=True)
    wx_free3 = models.CharField(max_length=45, blank=True, null=True)
    wx_free4 = models.CharField(max_length=45, blank=True, null=True)
    wx_free5 = models.CharField(max_length=45, blank=True, null=True)
    wx_number = models.CharField(max_length=60)
    etl_flag = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wx_user_infos'
        unique_together = (('id', 'wx_number'),)


class WxUserInfosNh(models.Model):
    id = models.IntegerField(primary_key=True)
    wx_userid = models.CharField(max_length=150)
    wx_alisa = models.CharField(max_length=100, blank=True, null=True)
    wx_truename = models.CharField(max_length=45, blank=True, null=True)
    wx_headid = models.CharField(max_length=300, blank=True, null=True)
    wx_mobile = models.CharField(max_length=45, blank=True, null=True)
    wx_nickname = models.CharField(max_length=200, blank=True, null=True)
    wx_signature = models.CharField(max_length=200, blank=True, null=True)
    wx_remark = models.CharField(max_length=200, blank=True, null=True)
    wx_guestid = models.CharField(max_length=45, blank=True, null=True)
    wx_flag = models.IntegerField(blank=True, null=True)
    wx_createtime = models.BigIntegerField(blank=True, null=True)
    wx_updatetime = models.BigIntegerField(blank=True, null=True)
    wx_deltime = models.BigIntegerField(blank=True, null=True)
    wx_type = models.IntegerField(blank=True, null=True)
    wx_verifyflag = models.IntegerField(db_column='wx_verifyFlag', blank=True, null=True)  # Field name made lowercase.
    wx_usertype = models.CharField(max_length=45, blank=True, null=True)
    wx_pinyin_full = models.CharField(max_length=100, blank=True, null=True)
    wx_pinyin_first = models.CharField(max_length=45, blank=True, null=True)
    wx_time_fix = models.SmallIntegerField(blank=True, null=True)
    wx_labels = models.TextField(blank=True, null=True)
    wx_free1 = models.CharField(max_length=45, blank=True, null=True)
    wx_free2 = models.CharField(max_length=45, blank=True, null=True)
    wx_free3 = models.CharField(max_length=45, blank=True, null=True)
    wx_free4 = models.CharField(max_length=45, blank=True, null=True)
    wx_free5 = models.CharField(max_length=45, blank=True, null=True)
    wx_number = models.CharField(max_length=60)
    etl_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wx_user_infos_nh'
        unique_together = (('id', 'wx_number'),)


class WxUserMessages(models.Model):
    wx_msg_id = models.PositiveIntegerField(primary_key=True)
    wx_userid = models.CharField(max_length=150, blank=True, null=True)
    wx_touserid = models.CharField(max_length=150, blank=True, null=True)
    msg_type = models.CharField(max_length=30, blank=True, null=True)
    msg_flag = models.PositiveIntegerField(blank=True, null=True)
    msg_isme = models.PositiveSmallIntegerField(blank=True, null=True)
    msg_content = models.TextField(blank=True, null=True)
    msg_time = models.BigIntegerField(blank=True, null=True)
    msg_createtime = models.BigIntegerField(blank=True, null=True)
    msg_serverid = models.CharField(max_length=60, blank=True, null=True)
    wx_number = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'wx_user_messages'
        unique_together = (('wx_msg_id', 'wx_number'),)


class WxUserMessagesNh(models.Model):
    wx_msg_id = models.IntegerField(primary_key=True)
    wx_userid = models.CharField(max_length=150, blank=True, null=True)
    wx_touserid = models.CharField(max_length=150, blank=True, null=True)
    msg_type = models.CharField(max_length=30, blank=True, null=True)
    msg_flag = models.IntegerField(blank=True, null=True)
    msg_isme = models.SmallIntegerField(blank=True, null=True)
    msg_content = models.TextField(blank=True, null=True)
    msg_time = models.BigIntegerField(blank=True, null=True)
    msg_createtime = models.BigIntegerField(blank=True, null=True)
    msg_serverid = models.CharField(max_length=60, blank=True, null=True)
    wx_number = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'wx_user_messages_nh'
        unique_together = (('wx_msg_id', 'wx_number'),)
