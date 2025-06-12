import re
import numpy as np

def extract_sections(report):
    """
    Extract standard sections from a radiology report.
    
    Args:
        report (str): The radiology report text
        
    Returns:
        dict: Dictionary containing extracted sections
    """
    # Define common section headers
    section_patterns = {
        "clinical_info": r"(?:CLINICAL|INDICATION|HISTORY).*?:",
        "technique": r"(?:TECHNIQUE|PROCEDURE).*?:",
        "findings": r"(?:FINDINGS|RESULT).*?:",
        "impression": r"(?:IMPRESSION|CONCLUSION|ASSESSMENT).*?:"
    }
    
    sections = {}
    
    # Extract each section
    for section_name, pattern in section_patterns.items():
        match = re.search(f"{pattern}(.*?)(?={''|'.join(list(section_patterns.values()))}|$)", 
                         report, 
                         re.DOTALL | re.IGNORECASE)
        if match:
            sections[section_name] = match.group(1).strip()
        else:
            sections[section_name] = ""
    
    return sections

def extract_measurements(text):
    """
    Extract measurements from text.
    
    Args:
        text (str): Text containing measurements
        
    Returns:
        list: List of extracted measurements with units
    """
    # Pattern for measurements: number + optional decimal + optional space + unit
    pattern = r"(\d+\.?\d*)\s*(mm|cm|ml|cc|Hz|HU)"
    measurements = re.findall(pattern, text, re.IGNORECASE)
    
    return [{"value": float(value), "unit": unit.lower()} for value, unit in measurements]

def normalize_anatomical_terms(text):
    """
    Normalize anatomical terms to standard terminology.
    
    Args:
        text (str): Text containing anatomical terms
        
    Returns:
        str: Text with normalized anatomical terms
    """
    # Example normalization mappings
    replacements = {
        r"\brt\b": "right",
        r"\blt\b": "left",
        r"\bant\b": "anterior",
        r"\bpost\b": "posterior",
        r"\bsup\b": "superior",
        r"\binf\b": "inferior",
        r"\bmed\b": "medial",
        r"\blat\b": "lateral"
    }
    
    normalized = text
    for pattern, replacement in replacements.items():
        normalized = re.sub(pattern, replacement, normalized, flags=re.IGNORECASE)
    
    return normalized