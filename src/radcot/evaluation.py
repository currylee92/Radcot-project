import numpy as np
from sklearn.metrics import precision_recall_fscore_support, cohen_kappa_score

class RadCoTEvaluator:
    """Evaluator for RadCoT framework performance."""
    
    def __init__(self):
        """Initialize RadCoT evaluator."""
        pass
    
    def evaluate(self, predictions, ground_truth):
        """
        Evaluate error detection performance.
        
        Args:
            predictions (list): List of predicted errors
            ground_truth (list): List of ground truth errors
            
        Returns:
            dict: Evaluation metrics
        """
        # Match predictions to ground truth
        matched_predictions, matched_ground_truth = self._match_errors(predictions, ground_truth)
        
        # Calculate metrics
        precision, recall, f1, _ = precision_recall_fscore_support(
            matched_ground_truth, 
            matched_predictions, 
            average='binary'
        )
        
        return {
            "precision": precision,
            "recall": recall,
            "f1": f1
        }
    
    def evaluate_by_error_type(self, predictions, ground_truth):
        """
        Evaluate error detection performance by error type.
        
        Args:
            predictions (list): List of predicted errors with type information
            ground_truth (list): List of ground truth errors with type information
            
        Returns:
            dict: Evaluation metrics by error type
        """
        error_types = set([error["type"] for error in ground_truth])
        results = {}
        
        for error_type in error_types:
            # Filter errors by type
            type_predictions = [error for error in predictions if error["type"] == error_type]
            type_ground_truth = [error for error in ground_truth if error["type"] == error_type]
            
            # Evaluate for this error type
            type_results = self.evaluate(type_predictions, type_ground_truth)
            results[error_type] = type_results
        
        return results
    
    def evaluate_by_modality(self, predictions, ground_truth, modalities):
        """
        Evaluate error detection performance by modality.
        
        Args:
            predictions (dict): Dictionary of predicted errors by report ID
            ground_truth (dict): Dictionary of ground truth errors by report ID
            modalities (dict): Dictionary mapping report IDs to modalities
            
        Returns:
            dict: Evaluation metrics by modality
        """
        modality_types = set(modalities.values())
        results = {}
        
        for modality in modality_types:
            # Filter reports by modality
            modality_report_ids = [report_id for report_id, mod in modalities.items() if mod == modality]
            
            # Filter errors by modality
            modality_predictions = {report_id: predictions[report_id] for report_id in modality_report_ids if report_id in predictions}
            modality_ground_truth = {report_id: ground_truth[report_id] for report_id in modality_report_ids if report_id in ground_truth}
            
            # Flatten for evaluation
            flat_predictions = [error for report in modality_predictions.values() for error in report]
            flat_ground_truth = [error for report in modality_ground_truth.values() for error in report]
            
            # Evaluate for this modality
            modality_results = self.evaluate(flat_predictions, flat_ground_truth)
            results[modality] = modality_results
        
        return results
    
    def calculate_intermodel_agreement(self, model1_predictions, model2_predictions, ground_truth):
        """
        Calculate agreement between two models.
        
        Args:
            model1_predictions (list): Predictions from first model
            model2_predictions (list): Predictions from second model
            ground_truth (list): Ground truth errors
            
        Returns:
            float: Cohen's kappa coefficient
        """
        # Match predictions to ground truth
        matched_model1, _ = self._match_errors(model1_predictions, ground_truth)
        matched_model2, _ = self._match_errors(model2_predictions, ground_truth)
        
        # Calculate Cohen's kappa
        kappa = cohen_kappa_score(matched_model1, matched_model2)
        
        return kappa
    
    def _match_errors(self, predictions, ground_truth):
        """
        Match predicted errors to ground truth errors.
        
        Args:
            predictions (list): List of predicted errors
            ground_truth (list): List of ground truth errors
            
        Returns:
            tuple: Binary arrays of matched predictions and ground truth
        """
        # Implementation of error matching logic
        # This is a simplified version - real implementation would need more sophisticated matching
        
        matched_predictions = np.zeros(len(ground_truth), dtype=int)
        matched_ground_truth = np.ones(len(ground_truth), dtype=int)
        
        for i, gt_error in enumerate(ground_truth):
            for pred_error in predictions:
                if self._errors_match(gt_error, pred_error):
                    matched_predictions[i] = 1
                    break
        
        return matched_predictions, matched_ground_truth
    
    def _errors_match(self, error1, error2):
        """
        Determine if two errors match.
        
        Args:
            error1 (dict): First error
            error2 (dict): Second error
            
        Returns:
            bool: True if errors match, False otherwise
        """
        # Implementation of error matching criteria
        # This is a simplified version - real implementation would need more sophisticated matching
        
        # Example: Match if location and type are the same
        return (error1.get("location") == error2.get("location") and 
                error1.get("type") == error2.get("type"))