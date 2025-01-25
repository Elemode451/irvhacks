package com.irvhacks;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.openai.core.JsonValue;
import com.openai.models.ChatCompletion;
import com.openai.models.ChatCompletionCreateParams;
import com.openai.models.ChatCompletionUserMessageParam;
import com.openai.models.ChatModel;

@RestController
public class QueryManager {
    
    public static final String SEARCH_INFO = "You are to embody the role of a search engine." 
     + "You will only provide names in response to the" 
     + "query that is asked, with no other additional information." 
     + "You will provide a list of up to 10 names. JUST names. Seperate each one with the character |."; 
    
    public static final String DOCTOR_NAME = "If you are provided with a singular name, or asked for information on a name, just output the exact name back."; 
    
    
    @PostMapping("/query")    
    public void query(@RequestBody String query)
    {
        if (query == null || query.isEmpty()) {
          Main.message = "NO!";
        }
        ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
        .addMessage(ChatCompletionUserMessageParam.builder()
          .role(JsonValue.from("system"))
          .content(QueryManager.SEARCH_INFO)
          .build())
        .addMessage(ChatCompletionUserMessageParam.builder()
          .role(JsonValue.from("system"))
          .content(QueryManager.DOCTOR_NAME)
          .build())
        .addMessage(ChatCompletionUserMessageParam.builder()
          .role(JsonValue.from("user"))
          .content(query)
          .build())
        .model(ChatModel.GPT_4O_2024_11_20)
        .temperature(0.7)
        .build();

        ChatCompletion chatCompletion = client.chat().completions().create(params).validate();  
        Main.message = chatCompletion.choices().get(0).message().content().get();                                                                 
    }
    


}
