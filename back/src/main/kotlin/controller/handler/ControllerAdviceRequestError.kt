package com.cybergames.controller.handler

import com.cybergames.service.exceptions.UserNotFoundException
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.ControllerAdvice
import org.springframework.web.bind.annotation.ExceptionHandler
import org.springframework.web.context.request.WebRequest
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler

@ControllerAdvice
class ControllerAdviceRequestError : ResponseEntityExceptionHandler() {
    @ExceptionHandler(value = [UserNotFoundException::class])
    fun handleUserNotFound(ex: UserNotFoundException,request: WebRequest): ResponseEntity<String> {
        val errorDetails = "User not found"
        return ResponseEntity(errorDetails, HttpStatus.BAD_REQUEST)
    }
}