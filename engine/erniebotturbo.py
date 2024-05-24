# 文心一言旗舰版
from django.http import HttpResponse
import erniebot
import logging
from scalecraft import settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_erniebot():
    """配置和初始化 Erniebot 客户端"""
     # 假设已经有这个模块
    erniebot.api_type = settings.ERNIEBOT_API_TURBO_TYPE
    erniebot.access_token = settings.ERNIEBOT_ACCESS_TURBO_TOKEN
    return erniebot
def erniebotturbo(request):
    # 从请求中获取参数
    query = request.POST.get('query', '')
    # 处理逻辑
    if query:
        result = process_query(query)
    else:
        result = "process_query no query provided"

    # 生成响应
    return HttpResponse(result)

def process_query(query):
    """处理查询，发送到 AI Studio 并返回结果"""
    try:
        response = erniebot.ChatCompletion.create(
            model= settings.ERNIEBOT_ACCESS_35_TOKEN_MODEL,
            messages=[{
                'role': 'user',
                'content': query
            }]
        )
        result = response.get_result()
        logging.INFO(f"erniebotturbo process_query Resonpse is : {result}" )
        return result
    except Exception as e:
        logging.error(f"Failed to process query: {e}")
        return None








