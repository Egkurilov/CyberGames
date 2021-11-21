package service

import com.cybergames.ServerKt
import com.cybergames.entities.User
import com.cybergames.service.UserService
import org.apache.commons.lang3.ObjectUtils.isEmpty
import org.apache.commons.lang3.ObjectUtils.isNotEmpty
import org.junit.Test
import org.junit.runner.RunWith
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.test.context.junit4.SpringRunner
import kotlin.test.assertTrue

@RunWith(SpringRunner::class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT,
    classes = [ServerKt::class])
class UserServiceTest{
    @Autowired
    lateinit var userService: UserService

    @Test
    fun addUser(){
        assertTrue(isEmpty(userService.findAll()))
        userService.create(getUser())
        val users = userService.findAll()
        assertTrue(isNotEmpty(users))
    }
    private fun getUser(): User {
        return User("login", "fn", "ln",
            "superuser", "mail@mail.ru")
    }
}