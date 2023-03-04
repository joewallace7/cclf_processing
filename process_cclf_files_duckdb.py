import duckdb, os

def main():
    process_files()
    return


# ==============================================================================
# OPTIONS AND FILE FORMAT SETTINGS

# SQLite database file name
DBNAME = 'cclf_data.duckdb'

# Establish SQLite Database connection
cnx = duckdb.connect(DBNAME)

# Get file name list
file_list = os.listdir()
file_list = [x for x in file_list if x.startswith('P.')]

# Look up format based on file name
file_name_xwalk = {
    'ZC1' : 'CCLF1',
    'ZC2' : 'CCLF2',
    'ZC3' : 'CCLF3',
    'ZC4' : 'CCLF4',
    'ZC5' : 'CCLF5',
    'ZC6' : 'CCLF6',
    'ZC7' : 'CCLF7',
    'ZC8' : 'CCLF8',
    'ZC9' : 'CCLF9',
}


# File formats from:
#    https://www.cms.gov/files/document/cclf-file-data-elements-resource.pdf
# Format: [Column_name,start_position,end_postition]

file_formats = {}

file_formats['CCLF1'] = [
    ['CUR_CLM_UNIQ_ID',1,13],
    ['PRVDR_OSCAR_NUM',14,19],
    ['BENE_MBI_ID',20,30],
    ['BENE_HIC_NUM',31,41],
    ['CLM_TYPE_CD',42,43],
    ['CLM_FROM_DT',44,53],
    ['CLM_THRU_DT',54,63],
    ['CLM_BILL_FAC_TYPE_CD',64,64],
    ['CLM_BILL_CLSFCTN_CD',65,65],
    ['PRNCPL_DGNS_CD',66,72],
    ['ADMTG_DGNS_CD',73,79],
    ['CLM_MDCR_NPMT_RSN_CD',80,81],
    ['CLM_PMT_AMT',82,98],
    ['CLM_NCH_PRMRY_PYR_CD',99,99],
    ['PRVDR_FAC_FIPS_ST_CD',100,101],
    ['BENE_PTNT_STUS_CD',102,103],
    ['DGNS_DRG_CD',104,107],
    ['CLM_OP_SRVC_TYPE_CD',108,108],
    ['FAC_PRVDR_NPI_NUM',109,118],
    ['OPRTG_PRVDR_NPI_NUM',119,128],
    ['ATNDG_PRVDR_NPI_NUM',129,138],
    ['OTHR_PRVDR_NPI_NUM',139,148],
    ['CLM_ADJSMT_TYPE_CD',149,150],
    ['CLM_EFCTV_DT',151,160],
    ['CLM_IDR_LD_DT',161,170],
    ['BENE_EQTBL_BIC_HICN_NUM',171,181],
    ['CLM_ADMSN_TYPE_CD',182,183],
    ['CLM_ADMSN_SRC_CD',184,185],
    ['CLM_BILL_FREQ_CD',186,186],
    ['CLM_QUERY_CD',187,187],
    ['DGNS_PRCDR_ICD_IND',188,188],
    ['CLM_MDCR_INSTNL_TOT',189,203],
    ['CLM_MDCR_IP_PPS_CPTL_IME_AMT',204,218],
    ['CLM_OPRTNL_IME_AMT',219,240],
    ['CLM_MDCR_IP_PPS_DSP_RPRTNT_AMT',241,255],
    ['CLM_HIPPS_UNCOMPD_CARE_AMT',256,270],
    ['CLM_OPRTNL_DSPRPRTNT_AMT',271,292],
    ['ADDITIONAL_COLUMNS',293,1000]
]

file_formats['CCLF2'] =[
    ['CUR_CLM_UNIQ_ID',1,13],
    ['CLM_LINE_NUM',13,23],
    ['BENE_MBI_ID',24,34],
    ['BENE_HIC_NUM',35,45],
    ['CLM_TYPE_CD',46,47],
    ['CLM_LINE_FROM_DT',48,57],
    ['CLM_LINE_THRU_DT',58,67],
    ['CLM_LINE_PROD_REV_CTR_CD',68,71],
    ['CLM_LINE_INSTNL_REV_CTR_DT',72,81],
    ['CLM_LINE_HCPCS_CD',82,86],
    ['BENE_EQTBL_BIC_HICN_NUM',87,97],
    ['PRVDR_OSCAR_NUM',98,103],
    ['CLM_FROM_DT',104,113],
    ['CLM_THRU_DT',114,123],
    ['CLM_LINE_SRVC_UNIT_QTY',124,147],
    ['CLM_LINE_CVRD_PD_AMT',148,164],
    ['HCPCS_1_MDFR_CD',165,166],
    ['HCPCS_2_MDFR_CD',167,168],
    ['HCPCS_3_MDFR_CD',169,170],
    ['HCPCS_4_MDFR_CD',171,172],
    ['HCPCS_5_MDFR_CD',173,174],
    ['CLM_REV_APC_HIPPS_CD',175,179],
]

file_formats['CCLF3'] = [
    ['CUR_CLM_UNIQ_ID',1,13],
    ['BENE_MBI_ID',14,24],
    ['BENE_HIC_NUM',25,35],
    ['CLM_TYPE_CD',36,37],
    ['CLM_VAL_SQNC_NUM',38,39],
    ['CLM_PRCDR_CD',40,46],
    ['CLM_PRCDR_PRFRM_DT',47,56],
    ['BENE_EQTBL_BIC_HICN_NUM',57,67],
    ['PRVDR_OSCAR_NUM',68,73],
    ['CLM_FROM_DT',74,83],
    ['CLM_THRU_DT',84,93],
    ['DGNS_PRCDR_ICD_IND',94,94],
]

file_formats['CCLF4'] = [
    ['CUR_CLM_UNIQ_ID',1,13],
    ['BENE_MBI_ID',14,24],
    ['BENE_HIC_NUM',25,35],
    ['CLM_TYPE_CD',36,37],
    ['CLM_PROD_TYPE_CD',38,38],
    ['CLM_VAL_SQNC_NUM',39,40],
    ['CLM_DGNS_CD',41,47],
    ['BENE_EQTBL_BIC_HICN_NUM',48,58],
    ['PRVDR_OSCAR_NUM',59,64],
    ['CLM_FROM_DT',65,74],
    ['CLM_THRU_DT',75,84],
    ['CLM_POA_IND',85,91],
    ['DGNS_PRCDR_ICD_IND',92,92],
]

file_formats['CCLF5'] = [
    ['CUR_CLM_UNIQ_ID',1,13],
    ['CLM_LINE_NUM',14,23],
    ['BENE_MBI_ID',24,34],
    ['BENE_HIC_NUM',35,45],
    ['CLM_TYPE_CD',46,47],
    ['CLM_FROM_DT',48,57],
    ['CLM_THRU_DT',58,67],
    ['RNDRG_PRVDR_TYPE_CD',68,70],
    ['RNDRG_PRVDR_FIPS_ST_CD',71,72],
    ['CLM_PRVDR_SPCLTY_CD',73,74],
    ['CLM_FED_TYPE_SRVC_CD',75,75],
    ['CLM_POS_CD',76,77],
    ['CLM_LINE_FROM_DT',78,87],
    ['CLM_LINE_THRU_DT',88,97],
    ['CLM_LINE_HCPCS_CD',98,102],
    ['CLM_LINE_CVRD_PD_AMT',103,117],
    ['CLM_LINE_PRMRY_PYR_CD',118,118],
    ['CLM_LINE_DGNS_CD',119,125],
    ['CLM_RNDRG_PRVDR_TAX_NUM',126,135],
    ['RNDRG_PRVDR_NPI_NUM',136,145],
    ['CLM_CARR_PMT_DNL_CD',146,147],
    ['CLM_PRCSG_IND_CD',148,149],
    ['CLM_ADJSMT_TYPE_CD',150,151],
    ['CLM_EFCTV_DT',152,161],
    ['CLM_IDR_LD_DT',162,171],
    ['CLM_CNTL_NUM',172,211],
    ['BENE_EQTBL_BIC_HICN_NUM',212,222],
    ['CLM_LINE_ALOWD_CHRG_AMT',223,239],
    ['CLM_LINE_SRVC_UNIT_QTY',240,263],
    ['HCPCS_1_MDFR_CD',264,265],
    ['HCPCS_2_MDFR_CD',266,267],
    ['HCPCS_3_MDFR_CD',268,269],
    ['HCPCS_4_MDFR_CD',270,271],
    ['HCPCS_5_MDFR_CD',272,273],
    ['CLM_DISP_CD',274,275],
    ['CLM_DGNS_1_CD',276,282],
    ['CLM_DGNS_2_CD',283,289],
    ['CLM_DGNS_3_CD',290,296],
    ['CLM_DGNS_4_CD',297,303],
    ['CLM_DGNS_5_CD',304,310],
    ['CLM_DGNS_6_CD',311,317],
    ['CLM_DGNS_7_CD',318,324],
    ['CLM_DGNS_8_CD',325,331],
    ['DGNS_PRCDR_ICD_IND',332,332],
    ['CLM_DGNS_9_CD',333,339],
    ['CLM_DGNS_10_CD',340,346],
    ['CLM_DGNS_11_CD',347,353],
    ['CLM_DGNS_12_CD',354,360],
    ['HCPCS_BETOS_CD',361,363],
]


file_formats['CCLF6'] = [
    ['CUR_CLM_UNIQ_ID',1,13],
    ['CLM_LINE_NUM',14,23],
    ['BENE_MBI_ID',24,34],
    ['BENE_HIC_NUM',35,45],
    ['CLM_TYPE_CD',46,47],
    ['CLM_FROM_DT',48,57],
    ['CLM_THRU_DT',58,67],
    ['CLM_FED_TYPE_SRVC_CD',68,68],
    ['CLM_POS_CD',69,70],
    ['CLM_LINE_FROM_DT',71,80],
    ['CLM_LINE_THRU_DT',81,90],
    ['CLM_LINE_HCPCS_CD',91,95],
    ['CLM_LINE_CVRD_PD_AMT',96,110],
    ['CLM_PRMRY_PYR_CD',111,111],
    ['PAYTO_PRVDR_NPI_NUM',112,121],
    ['ORDRG_PRVDR_NPI_NUM',122,131],
    ['CLM_CARR_PMT_DNL_CD',132,133],
    ['CLM_PRCSG_IND_CD',134,135],
    ['CLM_ADJSMT_TYPE_CD',136,137],
    ['CLM_EFCTV_DT',138,147],
    ['CLM_IDR_LD_DT',148,157],
    ['CLM_CNTL_NUM',158,197],
    ['BENE_EQTBL_BIC_HICN_NUM',198,208],
    ['CLM_LINE_ALOWD_CHRG_AMT',209,225],
    ['CLM_DISP_CD',226,227],
]

file_formats['CCLF7'] = [
    ['CUR_CLM_UNIQ_ID',1,13],
    ['BENE_MBI_ID',14,24],
    ['BENE_HIC_NUM',25,35],
    ['CLM_LINE_NDC_CD',36,46],
    ['CLM_TYPE_CD',47,48],
    ['CLM_LINE_FROM_DT',49,58],
    ['PRVDR_SRVC_ID_QLFYR_CD',59,60],
    ['CLM_SRVC_PRVDR_GNRC_ID_NUM',61,80],
    ['CLM_DSPNSNG_STUS_CD',81,81],
    ['CLM_DAW_PROD_SLCTN_CD',82,82],
    ['CLM_LINE_SRVC_UNIT_QTY',83,106],
    ['CLM_LINE_DAYS_SUPLY_QTY',107,115],
    ['PRVDR_PRSBNG_ID_QLFYR_CD',116,117],
    ['CLM_PRSBNG_PRVDR_GNRC_ID_NUM',118,137],
    ['CLM_LINE_BENE_PMT_AMT',138,150],
    ['CLM_ADJSMT_TYPE_CD',151,152],
    ['CLM_EFCTV_DT',153,162],
    ['CLM_IDR_LD_DT',163,172],
    ['CLM_LINE_RX_SRVC_RFRNC_NUM',173,184],
    ['CLM_LINE_RX_FILL_NUM',185,193],
    ['CLM_PHRMCY_SRVC_TYPE_CD',194,195],
]


file_formats['CCLF8'] = [
    ['BENE_MBI_ID',1,11],
    ['BENE_HIC_NUM',12,22],
    ['BENE_FIPS_STATE_CD',23,24],
    ['BENE_FIPS_CNTY_CD',25,27],
    ['BENE_ZIP_CD',28,32],
    ['BENE_DOB',33,42],
    ['BENE_SEX_CD',43,43],
    ['BENE_RACE_CD',44,44],
    ['BENE_AGE',45,47],
    ['BENE_MDCR_STUS_CD',48,49],
    ['BENE_DUAL_STUS_CD',50,51],
    ['BENE_DEATH_DT',52,61],
    ['BENE_RNG_BGN_DT',62,71],
    ['BENE_RNG_END_DT',72,81],
    ['BENE_1ST_NAME',82,111],
    ['BENE_MIDL_NAME',112,126],
    ['BENE_LAST_NAME',127,166],
    ['BENE_ORGNL_ENTLMT_RSN_CD',167,167],
    ['BENE_ENTLMT_BUYIN_IND',168,168],
    ['BENE_PART_A_ENRLMT_BGN_DT',169,178],
    ['BENE_PART_B_ENRLMT_BGN_DT',179,188],
    ['BENE_LINE_1_ADR',189,233],
    ['BENE_LINE_2_ADR',234,278],
    ['BENE_LINE_3_ADR',278,318],
    ['BENE_LINE_4_ADR',319,358],
    ['BENE_LINE_5_ADR',359,398],
    ['BENE_LINE_6_ADR',399,438],
    ['GEO_ZIP_PLC_NAME',439,538],
    ['GEO_USPS_STATE_CD',539,540],
    ['GEO_ZIP5_CD',541,545],
    ['GEO_ZIP4_CD',546,549],
]

file_formats['CCLF9'] = [
    ['HICN_MBI_XREF_IND',1,1],
    ['CRNT_NUM',2,12],
    ['PRVS_NUM',13,23],
    ['PRVS_ID_EFCTV_DT',24,33],
    ['PRVS_ID_OBSLT_DT',34,43],
    ['BENE_RRB_NUM',44,55],
]

#===============================================================================
# Cycle through files and match to the file types to match and import
def process_files():
    for F in file_list:
        print(F)
        for XW in file_name_xwalk:
            if F.find(XW) >= 0:
                filetype = file_name_xwalk[XW]
                if filetype not in file_formats:
                    print("**WARNING: Couldn't find",filetype,'in the file_formats dictionary.')
                    break
                print('  Importing',F,'>>',filetype)
                import_records(F,filetype)
                break

#===============================================================================
# Use the file formats to extract fields and import to SQLite database
def import_records(thefile,theformat):
    '''Import the data using the file format'''

    print(theformat)

    format_info = file_formats[theformat]

    # Build the table with the columns
    sql = cnx.execute(f" drop table if exists {theformat}; ")
    cnx.commit()

    column_list = [x[0] for x in format_info]
    column_list_str = ''
    for c in column_list:
        column_list_str += f" {c} VARCHAR, "

    column_list_str = column_list_str.strip(', ') # Remove last, unneeded comma

    # Build SELECT statement using the column format info
    select_columns = ""
    for c in format_info:
        select_columns += f"\n trim(substr(column0,{c[1]},{c[2]-c[1]+1})) as {c[0]}, "

    select_columns = select_columns.strip(', ') # Remove last, unneeded comma

    query = f"""
    CREATE OR REPLACE TABLE {theformat} AS
    SELECT
    {select_columns}
    FROM read_csv_auto('{thefile}')
    """

    cnx.sql(query)



    return



#===============================================================================
# Run Main Function
main()
