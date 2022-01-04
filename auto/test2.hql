create table db_stage.Fact_SL_File_Ngay1 as 
select count(*),accesstime,cls from db_goc.dim_image_21 group by accesstime,cls;


CREATE table db_stage.Dim_path1 as select  path, modificationtime, accesstime,substr (path, locate(".",path)+1) as CLS  from db_goc.dim_image1;


create table db_stage.dim_cls1 as

select cls from db_goc.dim_image_21 group by cls ;

drop table db_goc.fsimage1 ;
drop table db_goc.dim_image1 ;
drop table db_goc.dim_image_21;
