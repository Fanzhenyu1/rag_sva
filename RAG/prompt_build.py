import os
import json
import helper

def prompt_build_design_analysis(docs_content, all_files, RAG_ENABLE = 0):
    with open('e:/mylife_yanjiu/project/rag_sva/rules_1/design_analysis_en.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    context_all = ""
    for rtl_path in all_files:
        if not os.path.isfile(rtl_path):
            print(f'{rtl_path} is not a file, skip it.')
            continue
        with open(rtl_path, 'r', encoding='utf-8') as f:
            context_all = context_all + f.read()
    if RAG_ENABLE:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', context_all)          # 填入RTL代码
            .replace(r'{context}', docs_content)       # 填入检索文档
        )
    else:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', context_all)               # 填入RTL代码
            .replace(r'{context}', "")       # 填入检索文档
        )
    return filled_prompt

def prompt_build_query_simplify(docs_content, rtl_files, RAG_ENABLE = 0):
    with open('e:/mylife_yanjiu/project/rag_sva/rules_1/query_simplify_en.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    rtl_code = ""
    for rtl_path in rtl_files:
        if not os.path.isfile(rtl_path):
            print(f'{rtl_path} is not a file, skip it.')
            continue
        with open(rtl_path, 'r', encoding='utf-8') as f:
            rtl_code = rtl_code + f.read()
    filled_prompt = (
        prompt_template
        .replace(r'{document}', rtl_code)               # 填入RTL代码
    )
    return filled_prompt

def prompt_build_comment_fill(docs_content, rtl_files, RAG_ENABLE = 0):
    with open('e:/mylife_yanjiu/project/rag_sva/rules_1/design_fill_comments_en.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    rtl_code = ""
    for rtl_path in rtl_files:
        if not os.path.isfile(rtl_path):
            print(f'{rtl_path} is not a file, skip it.')
            continue
        with open(rtl_path, 'r', encoding='utf-8') as f:
            rtl_code = rtl_code + f.read()
    if RAG_ENABLE:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)          # 填入RTL代码
            .replace(r'{context}', docs_content)       # 填入检索文档
        )
    else:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)               # 填入RTL代码
            .replace(r'{context}', "")       # 填入检索文档
        )
    return filled_prompt

def prompt_build_assets_identify(docs_content, rtl_files, RAG_ENABLE = 0):
    # with open('e:/mylife_yanjiu/project/rag_sva/rules/asset_identify_en.md', 'r', encoding='utf-8') as f:
    with open('e:/mylife_yanjiu/project/rag_sva/rules/asset_identify_en_2.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    rtl_code = ""
    for rtl_path in rtl_files:
        if not os.path.isfile(rtl_path):
            print(f'{rtl_path} is not a file, skip it.')
            continue
        with open(rtl_path, 'r', encoding='utf-8') as f:
            rtl_code = rtl_code + f.read()
    if RAG_ENABLE:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)          # 填入RTL代码
            .replace(r'{context}', docs_content)       # 填入检索文档
        )
    else:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)               # 填入RTL代码
            .replace(r'{context}', "")       # 填入检索文档
        )
    return filled_prompt


def prompt_build_testpoint_generation(docs_content, json_assets, rtl_files, RAG_ENABLE = 0):
    # with open('e:/mylife_yanjiu/project/rag_sva/rules/testpoint_generation_en.md', 'r', encoding='utf-8') as f:
    with open('e:/mylife_yanjiu/project/rag_sva/rules/testpoint_generation.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    rtl_code = ""
    for rtl_path in rtl_files:
        if not os.path.isfile(rtl_path):
            print(f'{rtl_path} is not a file, skip it.')
            continue
        with open(rtl_path, 'r', encoding='utf-8') as f:
            rtl_code = rtl_code + f.read()
    # 判断 json_assets 类型
    if isinstance(json_assets, (dict, list)):
        assets_str = json.dumps(json_assets, indent=4, ensure_ascii=False)
    else:
        assets_str = str(json_assets)
    if RAG_ENABLE:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)          # 填入RTL代码
            .replace(r'{security_assets}', assets_str)  # 填入安全资产
            .replace(r'{context}', docs_content)       # 填入检索文档
        )
    else:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)               # 填入RTL代码
            .replace(r'{security_assets}', assets_str)       # 填入安全资产
            .replace(r'{context}', "")       # 填入检索文档
        )
    return filled_prompt


def prompt_build_property_generation(docs_content, json_testpoint, rtl_files, RAG_ENABLE = 0):
    # with open('e:/mylife_yanjiu/project/rag_sva/rules/property_generation_en.md', 'r', encoding='utf-8') as f:
    with open('e:/mylife_yanjiu/project/rag_sva/rules/property_generation.md', 'r', encoding='utf-8') as f:    
        prompt_template = f.read()
    rtl_code = ""
    for rtl_path in rtl_files:
        if not os.path.isfile(rtl_path):
            print(f'{rtl_path} is not a file, skip it.')
            continue
        with open(rtl_path, 'r', encoding='utf-8') as f:
            rtl_code = rtl_code + f.read()
    # 判断 json_testpoint 类型
    if isinstance(json_testpoint, (dict, list)):
        testpoint_str = json.dumps(json_testpoint, indent=4, ensure_ascii=False)
    else:
        testpoint_str = str(json_testpoint)
    if RAG_ENABLE:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)          # 填入RTL代码
            .replace(r'{test_points}', testpoint_str)  # 填入安全资产
            .replace(r'{context}', docs_content)       # 填入检索文档
        )
    else:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)               # 填入RTL代码
            .replace(r'{test_points}', testpoint_str)       # 填入安全资产
            .replace(r'{context}', "")       # 填入检索文档
        )
    return filled_prompt

def prompt_build_property_generation_all(docs_content, rtl_files, RAG_ENABLE = 0):
    with open('e:/mylife_yanjiu/project/rag_sva/rules/property_generation_all.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    rtl_code = ""
    for rtl_path in rtl_files:
        if not os.path.isfile(rtl_path):
            print(f'{rtl_path} is not a file, skip it.')
            continue
        with open(rtl_path, 'r', encoding='utf-8') as f:
            rtl_code = rtl_code + f.read()
    if RAG_ENABLE:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)          # 填入RTL代码
            .replace(r'{context}', docs_content)       # 填入检索文档
        )
    else:
        filled_prompt = (
            prompt_template
            .replace(r'{document}', rtl_code)               # 填入RTL代码
            .replace(r'{context}', "")       # 填入检索文档
        )
    return filled_prompt

def prompt_build_sva_simplify(sva_content):
    with open('e:/mylife_yanjiu/project/rag_sva/rules/sva_simplify_en.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    filled_prompt = (
        prompt_template
        .replace(r'{sva_content}', sva_content)          # 填入SVA内容
    )
    return filled_prompt