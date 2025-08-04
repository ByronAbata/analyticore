package com.analyticore.service;

public class KeywordExtractionService {
  public String[] extractKeywords(String text) {
    return text.split(" ");
  }
}
