# RadCoT Error Types

This document describes the error types that RadCoT is designed to detect in radiology reports.

## 1. Typographical Errors

Basic text errors including misspellings, grammatical errors, and punctuation mistakes.

**Examples:**
- Misspelling of anatomical terms (e.g., "adnominal" instead of "abdominal")
- Incorrect pluralization (e.g., "kidnies" instead of "kidneys")
- Basic grammar errors

## 2. Numerical Errors

Mistakes in measurements, values, or units.

**Examples:**
- Incorrect measurement values (e.g., "2.5 cm" when it should be "3.5 cm")
- Wrong units (e.g., "mm" instead of "cm")
- Implausible measurements (e.g., "15 cm kidney" for an adult)

## 3. Findings-Impression Discrepancies

Inconsistencies between the detailed findings section and the summary impression section.

**Examples:**
- A finding described in the findings section but omitted from the impression
- A conclusion in the impression that is not supported by any finding
- Contradictory descriptions of the same finding

## 4. Omission/Insertion Errors

Missing important information or inappropriately added content.

**Examples:**
- Failure to mention a critical anatomical structure that should be evaluated
- Missing follow-up recommendations for significant findings
- Including findings from a different patient

## 5. Interpretation Errors

Mistakes in the clinical interpretation or diagnostic conclusions.

**Examples:**
- Concluding benign when findings are suspicious for malignancy
- Misclassification of pathology
- Inappropriate level of diagnostic certainty