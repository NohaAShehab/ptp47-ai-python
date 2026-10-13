import  logging
# dealing with file/ stream/ network / db --> wrap script in try and except
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('file_ops')
# try:
#     file_obj = open("mycv.txt", 'r')
#     print(file_obj)
#
# except Exception as e:
#     print(e)
#     logger.error(f"error while opening file {e}")
#
#
# else:
#     # object refere to readbuffer
#     data  = file_obj.read()
#     print(data, type(data)) #string
#     # reset position to byte x
#     file_obj.seek(0)
#     data2 = file_obj.readlines() # list
#     print(data2, type(data2))
#
#     file_obj.close()
#




def read_line_by_line(file_name: str) -> list :
    """
    :param file_name:  the path of the file I need to read
    :return: list of lines or empty list if not exists
    """
    try:
        file_obj = open(file_name, 'r')
        logger.info(f"file opened successfully for reading ")
    except Exception as e:
        logger.error(f"error while opening file {e}")
        return []
    else:
        data = file_obj.readlines()
        if len(data) == 0: logger.info(f"the file is empty")
        file_obj.close()
        return data
    finally:
        logger.info(f"process of opening  file for read ended ")



###############################

def save_data_to_file(file_name : str, data : str) -> int| None :
    """

    :param file_name:
    :param data:
    :return:
    """
    try:
        file_obj = open(file_name, 'w')
        logger.info(f"file opened successfully for writing ")
    except Exception as e:
        logger.error(f"error while opening file {e}")
        return None
    else:
        total_written_bytes =file_obj.write(data)
        file_obj.close()
        return total_written_bytes
    finally:
        logger.info(f"process ended ")




########### Json
import json
















