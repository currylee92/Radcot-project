def load_prompts(use_radcot=True):
    """
    Load prompts for error detection in radiology reports.
    
    Args:
        use_radcot (bool): Whether to use RadCoT prompts or standard prompts
        
    Returns:
        dict: Dictionary of prompts
    """
    if use_radcot:
        return {
            "system": """You are a radiology quality assurance specialist tasked with detecting errors in radiology reports. 
                      Analyze each report using the Radiological Chain-of-Thought (RadCoT) framework.""",
            
            "anatomical_validation": """### Step 1: Anatomical Structure Validation
                                    Carefully review the following radiology report and identify any errors related to 
                                    anatomical references, laterality (left/right), or spatial relationships.
                                    
                                    Report:
                                    {report}
                                    
                                    1. Are all anatomical structures correctly named?
                                    2. Is laterality (left/right) consistently and correctly specified?
                                    3. Are spatial relationships anatomically accurate?
                                    4. Are there any contradictory anatomical descriptions?
                                    
                                    List all anatomical errors found:""",
            
            "measurement_consistency": """### Step 2: Measurement Consistency Checking
                                      Carefully review the following radiology report and identify any errors related to 
                                      measurements, units, or numerical values.
                                      
                                      Report:
                                      {report}
                                      
                                      1. Are all measurements provided with appropriate units?
                                      2. Are measurements consistent throughout the report?
                                      3. Are the measurements within physiologically plausible ranges?
                                      4. Are there any contradictory measurements?
                                      
                                      List all measurement errors found:""",
            
            "cross_sectional": """### Step 3: Cross-sectional Correlation
                              Carefully review the following radiology report and identify any inconsistencies 
                              between different imaging planes, sequences, or sections of the report.
                              
                              Report:
                              {report}
                              
                              1. Are findings consistent across different imaging planes/sequences?
                              2. Are there contradictions between descriptions of the same structure in different sections?
                              3. If multiple imaging techniques are mentioned, are their results compatible?
                              
                              List all cross-sectional correlation errors found:""",
            
            "findings_impression": """### Step 4: Findings-Impression Alignment
                                  Carefully review the following radiology report and identify any discrepancies 
                                  between the detailed findings section and the summary impression section.
                                  
                                  Report:
                                  {report}
                                  
                                  1. Are all significant findings from the findings section reflected in the impression?
                                  2. Are there any conclusions in the impression not supported by the findings?
                                  3. Are the impressions logically derived from the findings?
                                  
                                  List all findings-impression alignment errors found:""",
            
            "clinical_completeness": """### Step 5: Clinical Completeness Assessment
                                    Carefully review the following radiology report and identify any errors related to 
                                    missing clinically important information or follow-up recommendations.
                                    
                                    Report:
                                    {report}
                                    
                                    1. Based on the findings, are appropriate follow-up recommendations provided?
                                    2. Are there any clinically significant findings that appear to be overlooked?
                                    3. Is the report complete for the stated clinical indication?
                                    
                                    List all clinical completeness errors found:""",
            
            "terminology_accuracy": """### Step 6: Radiological Terminology Accuracy
                                   Carefully review the following radiology report and identify any errors related to 
                                   radiological terminology, lexicon, or standard reporting language.
                                   
                                   Report:
                                   {report}
                                   
                                   1. Is standard radiological terminology used appropriately?
                                   2. Are there any instances of incorrect or outdated terms?
                                   3. Are abbreviations used consistently and appropriately?
                                   
                                   List all terminology errors found:""",
            
            "final_prompt": """Based on your structured analysis using the RadCoT framework, 
                           provide a comprehensive list of all errors found in the report.
                           For each error, specify:
                           1. The error type
                           2. The location in the report
                           3. A brief explanation
                           4. Confidence level (high, medium, low)
                           
                           Report:
                           {report}"""
        }
    else:
        return {
            "system": """You are a radiology quality assurance specialist tasked with detecting errors in radiology reports.""",
            
            "standard": """Please review the following radiology report and identify any errors present. 
                        List each error you find with a brief explanation.
                        
                        Report:
                        {report}"""
        }