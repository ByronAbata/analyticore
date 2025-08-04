package com.analyticore.controller;

import com.analyticore.dto.AnalysisRequest;
import com.analyticore.dto.AnalysisResponse;
import com.analyticore.service.SentimentAnalysisService;
import com.analyticore.service.KeywordExtractionService;

import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin(origins = "*")
public class AnalysisController {

  private final SentimentAnalysisService sentimentService = new SentimentAnalysisService();
  private final KeywordExtractionService keywordService = new KeywordExtractionService();

  @GetMapping("/actuator/health")
  public String health() {
    return "OK";
  }

  @PostMapping("/analizar")
  public AnalysisResponse analyze(@RequestBody AnalysisRequest request) {
    try {
      // Realizar análisis
      double sentiment = sentimentService.analyzeSentiment(request.getText());
      String[] keywords = keywordService.extractKeywords(request.getText());
      
      // Crear respuesta
      AnalysisResponse response = new AnalysisResponse(
        request.getJobId(), 
        sentiment, 
        keywords
      );
      
      System.out.println("Análisis completado para job: " + request.getJobId());
      return response;
    } catch (Exception e) {
      System.err.println("Error en análisis: " + e.getMessage());
      throw new RuntimeException("Error procesando análisis", e);
    }
  }
}
