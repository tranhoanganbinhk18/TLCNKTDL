



LOAD DATA  INPATH '/home/hadoopuser/hadoop/hadoop_data/hdfs/namenode/current/fsimage/fsimage.csv' OVERWRITE INTO TABLE db_goc.fsimage1;


INSERT OVERWRITE TABLE db_goc.dim_image1 IF NOT EXISTS
select * from db_goc.fsimage1
where locate(".jpg",fsimage1.Path) != 0
or      locate(".png",fsimage1.Path) != 0
or      locate(".gif",fsimage1.Path) != 0
or      locate(".jpeg",fsimage1.Path) != 0 ;

INSERT OVERWRITE TABLE db_goc.dim_image_21 IF NOT EXISTS select  path, modificationtime, accesstime,substr (path, locate(".",path)+1) as CLS  from db_goc.dim_image1;


INSERT OVERWRITE TABLE db_stage.Fact_SL_File_Ngay1 IF NOT EXISTS
select count(*),accesstime,cls from db_goc.dim_image_21 group by accesstime,cls;


INSERT OVERWRITE TABLE db_stage.Dim_path1 IF NOT EXISTS
select  path, modificationtime, accesstime,substr (path, locate(".",path)+1) as CLS  from db_goc.dim_image1;


INSERT OVERWRITE table db_stage.dim_cls1 IF NOT EXISTS select cls from db_goc.dim_image_21 group by cls ;


INSERT OVERWRITE TABLE db_dwh.dim_cls
IF NOT EXISTS select * from db_stage.dim_cls1;

INSERT OVERWRITE TABLE db_dwh.dim_path
IF NOT EXISTS select * from db_stage.dim_path1;



INSERT OVERWRITE TABLE db_dwh.dwh_fact_tsl_file_ngay
IF NOT EXISTS select * from db_stage.fact_sl_file_ngay1;








