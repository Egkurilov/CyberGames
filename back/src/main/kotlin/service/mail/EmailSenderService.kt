package com.cybergames.service.mail

import com.cybergames.entities.User
import com.cybergames.properties.MailSenderProperties
import org.apache.commons.mail.DefaultAuthenticator
import org.apache.commons.mail.Email
import org.apache.commons.mail.SimpleEmail
import org.springframework.stereotype.Service


@Service
class EmailSenderService(
    val mailSenderProperties: MailSenderProperties) {
    fun sendEmail(user: User) {
        val email: Email = SimpleEmail()
        email.setHostName(mailSenderProperties.host)
        email.setSmtpPort(mailSenderProperties.port)
        email.setAuthenticator(DefaultAuthenticator(mailSenderProperties.username, mailSenderProperties.password))
        email.setSSLOnConnect(true)
        email.setFrom("user@gmail.com")
        email.setSubject("TestMail")
        email.setMsg("This is a test mail ... :-)")
        email.addTo("fkardashov@gmail.com")
        email.send()
    }
}