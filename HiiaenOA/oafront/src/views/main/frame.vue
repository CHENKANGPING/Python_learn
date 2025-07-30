<script setup name="frame">
import { ref, computed } from 'vue'
import {
    Expand,
    Fold,
} from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

let isCollapse = ref(false);
let asidWidth = computed(() => {
    if (isCollapse.value) {
        return '64px'
    } else {
        return '250px'
    }
})

const onCollapseAside = () => {
    isCollapse.value = !isCollapse.value;
}

const onExit = () =>{
    authStore.clearUerToken();
    router.push({name:'login'});
}
</script>

<template>
    <el-container class="container">
        <el-aside class="aside" :width="asidWidth">
            <router-link to="/" class="brand">
                <strong>Hiiaen</strong>
                <transition name="fade">
                    <span v-show="!isCollapse" class="brand-text">OA</span>
                </transition>
            </router-link>
            <el-menu default-active="1" class="el-menu-vertical-demo" background-color="#343a40" text-color="#fff"
                :collapse="isCollapse" :collapse-transition="false">
                <el-menu-item index="1">
                    <el-icon>
                        <HomeFilled />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon>
                            <Checked />
                        </el-icon>
                        <span>考勤管理</span>
                    </template>
                    <el-menu-item index="2-1">
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人考勤</span>
                    </el-menu-item>
                    <el-menu-item index="2-2">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>下属考勤</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>通知管理</span>
                    </template>
                    <el-menu-item index="3-1">
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>发布通知</span>
                    </el-menu-item>
                    <el-menu-item index="3-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>通知列表</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="4">
                    <template #title>
                        <el-icon>
                            <Avatar />
                        </el-icon>
                        <span>员工管理</span>
                    </template>
                    <el-menu-item index="4-1">
                        <el-icon>
                            <Plus />
                        </el-icon>
                        <span>新增员工</span>
                    </el-menu-item>
                    <el-menu-item index="4-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>员工列表</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-container>
            <el-header class="header">
                <div class="header-left">
                    <el-button class="collapse-btn" :icon="isCollapse ? Expand : Fold" @click="onCollapseAside" />
                </div>
                <el-dropdown>
                    <span class="el-dropdown-link">
                        <el-avatar :size="30" icon="UserFilled" />
                        <span style="margin-left: 4px;">[{{ authStore.user.department.name }}]{{authStore.user.realname}}</span>
                        <el-icon class="el-icon--right">
                            <arrow-down />
                        </el-icon>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item>修改密码</el-dropdown-item>
                            <el-dropdown-item divided @click="onExit">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
    transition: width 0.3s ease-in-out;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    white-space: nowrap;
}

.brand-text {
    margin-left: 4px;
}

.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.header-left {
    display: flex;
    align-items: center;

}

.el-dropdown-link{
    display: flex;
    align-items: center;
}

.el-menu {
    border-right: none;
}

.el-menu-item,
.el-sub-menu__title {
    color: #fff !important;
    transition: all 0.3s ease;
}

.el-menu-item:hover,
.el-sub-menu__title:hover {
    background-color: #364781 !important;
}

.collapse-btn {
    font-size: 18px;
    border: none;
    background: transparent;
    color: #606266;
    cursor: pointer;
    transition: all 0.3s ease;
}

.collapse-btn:hover {
    color: #409eff;
    transform: scale(1.1);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
